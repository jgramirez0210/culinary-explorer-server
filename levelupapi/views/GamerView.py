from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer

class GamerView(ViewSet):
    """Level up gamers view"""
    
    def list(self, request):
        """Handle GET requests to get all gamers """
        queryset = Gamer.objects.all()

        serializer = GamerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single gamer """
        try:
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer, many=False)
            return Response(serializer.data)
        except Gamer.DoesNotExist:
            return Response({'message': 'Gamer does not exist.'}, status=404)

    @classmethod
    def get_extra_actions(cls):
        return []
    
    def update(self, request, pk=None):
        """Handle PUT requests for a gamer"""
        try:
            gamer = Gamer.objects.get(pk=pk)
            gamer.bio = request.data.get('bio', gamer.bio)
            gamer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Gamer.DoesNotExist:
            return Response({'message': 'Gamer not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized gamer instance
        """
        # Assuming `uid` in the serializer corresponds to `userId` in the request data
        try:
            gamer = Gamer.objects.create(
                bio=request.data["bio"],
                uid=request.data["uid"], 
            )
            serializer = GamerSerializer(gamer, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Adding status code
        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        try:
            gamer = Gamer.objects.get(pk=pk)
            gamer.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Gamer.DoesNotExist:
            return Response({'message': 'Game not found.'}, status=status.HTTP_404_NOT_FOUND)        

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers
    """
    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'uid')