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