from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories
from .serializers import FoodLogSerializer

class FoodLogView(viewsets.ModelViewSet):    
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
        """Handle GET requests to get all food log entries
        
        Returns:
            Response -- JSON serialized list of food logs
        """
        try:
            food_log = Food_Log.objects.all()
            if not food_log.exists():
                return Response({'message': 'Food Log Entry not found'})
            serializer = FoodLogSerializer(food_log, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def create(self, request):
        """Handle POST requests to create a new food log entry
        
        Returns:
            Response -- JSON serialized 
        """
        serializer = FoodLogSerializer(data=request.data)
        if serializer.is_valid():
            food_log = serializer.save()
            food_log.category.set(request.data.get('category_ids', []))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    queryset = Food_Log.objects.all()
    serializer_class = FoodLogSerializer

    def update(self, request, pk=None):
        try:
            food_log = self.get_object()
            serializer = self.get_serializer(food_log, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """Delete food log entry"""
        try:
            food_log = Food_Log.objects.get(pk=pk)
            food_log.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)    
        except Food_Log.DoesNotExist:
            return Response(food_log.errors, status=status.HTTP_404_NOT_FOUND)    
        
            