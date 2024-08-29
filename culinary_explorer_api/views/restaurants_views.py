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
        