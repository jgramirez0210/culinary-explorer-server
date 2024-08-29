from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories
from .serializers import RestaurantSerializer


class RestaurantView(viewsets.ModelViewSet):
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
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            restaurants = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            restaurants = Restaurants.objects.get(pk=pk)
            restaurants.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Restaurants.DoesNotExist:
            return Response(restaurants.errors, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk):
        """Delete Restaurant"""
        try:
            restaurant = Restaurants.objects.get(pk=pk)
            restaurant.delete()        
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Restaurants.DoesNotExist:
            return Response(restaurant.errors, status=status.http404)