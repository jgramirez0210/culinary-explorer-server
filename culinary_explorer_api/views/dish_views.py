from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from culinary_explorer_api.models import Dish
from .serializers import DishSerializer

class DishView(viewsets.ModelViewSet):
    
    serializer_class = DishSerializer

    def get_queryset(self):
        return Dish.objects.all()
    
    def retrieve(self, request, pk):
        """Handel GET requests for single dish view
        
        Return:
            Response -- JSON serialized
        """
        try:
            dish = Dish.objects.get(pk=pk)
            serializer = DishSerializer(dish)
            return Response(serializer.data)
        except Dish.DoesNotExist:
            return Response({'message' : ' Dish not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to get all dishes
        
        Returns:
            Response -- JSON serialized list of food logs
        """
        try:
            dish = Dish.objects.all()
            if not dish.exists():
                return Response({'message' : 'Dish not found'})
            serializer = DishSerializer(dish, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)      
        
    def create(self, request):
        """Handle POST requests to create a new dish
        
        Returns:
            Response -- JSON serialized 
        """
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a dish
        
        Returns:
            Response -- JSON serialized
        """
        try:
            dish = Dish.objects.get(pk=pk)
            serializer = self.get_serializer(dish, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'message': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """Delete dish test"""
        try:
            dish = Dish.objects.get(pk=pk)
            dish.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Dish.DoesNotExist:
            return Response(dish.errors, status=status.HTTP_404_NOT_FOUND)