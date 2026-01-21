import logging
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories
from .serializers import RestaurantSerializer

logger = logging.getLogger(__name__)


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer
    
    def retrieve(self, request, pk):
        """Handel GET requests for a single restaurant
        
        Returns:
            Response -- JSON serialized"""
        try:
            restaurants = Restaurants.objects.get(pk=pk)
            serializer = RestaurantSerializer(restaurants)
            return Response(serializer.data)
        except Restaurants.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        """Handle GET requests to get all restaurant entries

        Returns:
            Response -- JSON serialized list of restaurants
        """
        logger.debug("RestaurantView.list called")
        try:
            restaurant = Restaurants.objects.all()
            if not restaurant.exists():
                return Response({'message': 'Restaurants not found'})
            serializer = RestaurantSerializer(restaurant, many = True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """Handle POST requests to create a new restaurant

        Returns:
            Response -- JSON serialized
        """
        data = request.data.copy()
        if request.user.is_authenticated:
            data['uid'] = request.user.id  # Use Django user ID if authenticated
        # If not authenticated, use the uid from payload (assuming it's validated client-side)
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            restaurant = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a restaurant"""
        try:
            restaurant = self.get_object()
            serializer = self.get_serializer(restaurant, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurants.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        """Delete Restaurant"""
        try:
            restaurant = Restaurants.objects.get(pk=pk)
            restaurant.delete()        
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Restaurants.DoesNotExist:
            return Response(restaurant.errors, status=status.http404)
        
    @action(detail=False, methods=['get'])
    def uid(self, request):
        """Retrieve restaurants by user ID"""
        user_id = request.query_params.get('uid', None)
        if user_id:
            restaurants = self.queryset.filter(uid=user_id)
            if restaurants.exists():
                serializer = self.get_serializer(restaurants, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No entries found for the given user ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'User ID not provided'}, status=status.HTTP_400_BAD_REQUEST)