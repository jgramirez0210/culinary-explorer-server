from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories
from .serializers import FoodLogSerializer

class FoodLogView(viewsets.ModelViewSet):
    
    queryset = Food_Log.objects.all()
    serializer_class = FoodLogSerializer
    
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
        
    def list(self, request, *args, **kwargs):
        """Handle GET requests for a list of food log entries
        
        Returns:
            Response -- JSON serialized 
        """
        try:
            food_log = self.get_queryset()
            if not food_log.exists():
                return Response({'message': 'Food Log Entry not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = FoodLogSerializer(food_log, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request, *args, **kwargs):
         serializer = self.get_serializer(data=request.data)
         if serializer.is_valid():
             food_log = serializer.save()
             food_log.category.set(request.data.get('category_ids', []))
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
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
            return Response({'error': 'Food log entry not found'}, status=status.HTTP_404_NOT_FOUND)    
        
    @action(detail=False, methods=['get'])
    def by_restaurant(self, request):
        """Retrieve food log entries by restaurant IDs"""
        restaurant_ids = request.query_params.get('restaurant_id', None)
        if restaurant_ids:
            restaurant_ids_list = restaurant_ids.split(',')
            food_logs = self.queryset.filter(restaurant_id__in=restaurant_ids_list)
            if food_logs.exists():
                serializer = self.get_serializer(food_logs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No entries found for the given restaurant IDs'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Restaurant ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def uid(self, request):
        """Retrieve food log entries by user ID"""
        user_id = request.query_params.get('uid', None)
        if user_id:
            food_logs = self.queryset.filter(uid=user_id)
            if food_logs.exists():
                serializer = self.get_serializer(food_logs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No entries found for the given user ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'User ID not provided'}, status=status.HTTP_400_BAD_REQUEST)