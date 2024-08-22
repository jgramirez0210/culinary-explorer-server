from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories
from rest_framework import serializers
from culinary_explorer_api.models import Food_Log, Restaurants, Dish, Categories

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'restaurant_name', 'restaurant_address', 'website_url']

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'dish_name', 'description', 'notes', 'food_image_url', 'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category']

class FoodLogSerializer(serializers.ModelSerializer):
    """JSON Serializer for food log"""
    restaurant = RestaurantSerializer(read_only=True)
    dish = DishSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurants.objects.all(), source='restaurant', write_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(), source='dish', write_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), source='category', many=True, write_only=True)

    class Meta:
        model = Food_Log
        fields = ['id', 'restaurant', 'dish', 'category', 'uid', 'restaurant_id', 'dish_id', 'category_ids']
        extra_kwargs = {
            'restaurant': {'required': False},
            'dish': {'required': False},
            'category': {'required': False},
        }
    
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
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        