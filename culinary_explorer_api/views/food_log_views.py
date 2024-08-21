from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from culinary_explorer_api.models import Food_Log

class FoodLogSerializer(serializers.ModelSerializer):
    """JSON Serializer for food log"""
    class Meta:
        model = Food_Log
        fields = ['restaurant', 'dish', 'category', 'uid']
    
class FoodLogView(ViewSet):    
    def retrieve(self, request, pk):
        """Handle GET requests for a single food log entry
        
        Returns:
            Response -- JSON serialized 
        """
        try:
            food_log = Food_Log.objects.get(pk=pk)
            serializer = FoodLogSerializer(food_log)
            return Response(serializer.data)
        except Food_Log.DoesNotExist:
            return Response({'message': 'Food Log Entry not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to get all food log entries"""
        try:
            food_log = Food_Log.objects.all()
            if not food_log.exists():
                return Response({'message': 'Food Log Entry not found'})
            serializer = FoodLogSerializer(food_log, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       