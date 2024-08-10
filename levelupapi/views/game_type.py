"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game_Type


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type
    
        Returns:
            Response -- JSON serialized game type
        """
        game_type = Game_Type.objects.filter(pk=pk).first()
    
        if game_type is None:
            return Response({'message': 'Game type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        try:
            game_types = Game_Type.objects.all()
            serializer = GameTypeSerializer(game_types, many=True)
            return Response(serializer.data)
        except Game_Type.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game_Type
        fields = ('id', 'label')
