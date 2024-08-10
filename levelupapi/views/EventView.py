from rest_framework import serializers
from levelupapi.models import Event, Gamer, EventGamer, Game

# Define the serializer outside of the EventView class
class EventViewSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'game', 'organizer', 'description', 'date', 'time', 'joined']

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

class EventView(viewsets.ModelViewSet):
    """Level up event types view"""
    queryset = Event.objects.all()
    serializer_class = EventViewSerializer
    # The rest of your EventView class definition remains unchanged

    def retrieve(self, request, pk):
        """Handle GET requests for single event type
        Returns:
            Response -- JSON serialized event type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventViewSerializer(event)
        return Response(serializer.data)

    
    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        serializer = EventViewSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(methods=['post', 'put'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
        
        # Use ID from request.data to get the gamer
        gamer_id = request.data["userId"]
        gamer = Gamer.objects.get(pk=gamer_id)  # Use pk to filter by ID
        event = Event.objects.get(pk=pk)
        attendee = EventGamer.objects.create(
            gamer=gamer,
            event=event
        )
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Handle DELETE requests to leave an event"""
        # Check if 'userId' is in request.data
        if 'userId' not in request.data:
            return Response({'message': 'userId is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            # Use ID from request.data to get the gamer
            gamer_id = request.data["userId"]
            gamer = Gamer.objects.get(pk=gamer_id)  # Use pk to filter by ID
            event = Event.objects.get(pk=pk)
    
            attendee = EventGamer.objects.get(gamer=gamer, event=event)
            attendee.delete()
    
            return Response({'message': 'Gamer removed'}, status=status.HTTP_204_NO_CONTENT)
        except Gamer.DoesNotExist:
            return Response({'message': 'Gamer does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Event.DoesNotExist:
            return Response({'message': 'Event does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except EventGamer.DoesNotExist:
            return Response({'message': 'Gamer is not registered for this event.'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized event instance
        """
        game = Game.objects.get(pk=request.data["gameId"])
        organizer_id = request.data["userId"] 
    
        organizer = Gamer.objects.get(pk=organizer_id)  
    
        event = Event.objects.create(
            game=game,
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer_id=organizer_id
        )
    
        serializer = EventViewSerializer(event, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an event
        Returns:
            Response -- Empty body with 204 status code or 404 if event does not exist
        """
        try:
            event = Event.objects.get(pk=pk)
            event.description = request.data["description"]
            event.date = request.data["date"]
            event.time = request.data["time"]
            event.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({'message': 'Event does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({'message': 'Event does not exist.'}, status=status.HTTP_404_NOT_FOUND)
