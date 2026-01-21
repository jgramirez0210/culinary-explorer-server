import logging
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from culinary_explorer_api.models import Dish
from .serializers import DishSerializer

logger = logging.getLogger(__name__)

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
        logger.debug("DishView.list called")
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
        logger.debug(f"DishView.create called with data: {request.data}")
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Dish created successfully: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.debug(f"Dish creation failed with errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a dish

        Returns:
            Response -- JSON serialized
        """
        logger.debug(f"DishView.update called with pk: {pk}, data: {request.data}")
        data = request.data
        if 'dish' in data:
            data = data['dish']
        # Handle None price gracefully by converting to empty string
        if 'price' in data and data['price'] is None:
            data['price'] = ''
        logger.debug(f"Using data: {data}")
        try:
            dish = self.get_object()
            logger.debug(f"Dish instance: {dish}")
            serializer = self.get_serializer(dish, data=data, partial=True)
            if serializer.is_valid():
                logger.debug(f"Validated data: {serializer.validated_data}")
                self.perform_update(serializer)
                logger.debug(f"Dish updated successfully: {serializer.data}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.debug(f"Dish update failed with errors: {serializer.errors}")
                return Response({
                    'errors': serializer.errors,
                    'redirect_to': f'/edit/dish/{pk}'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Dish.DoesNotExist:
            return Response({'message': 'Dish not found', 'redirect_to': f'/edit/dish/{pk}'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.debug(f"Dish update failed with exception: {str(ex)}")
            return Response({'error': str(ex), 'redirect_to': f'/edit/dish/{pk}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """Delete dish test"""
        try:
            dish = Dish.objects.get(pk=pk)
            dish.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Dish.DoesNotExist:
            return Response({'message': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)