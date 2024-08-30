from rest_framework import serializers
from culinary_explorer_api.models import Dish, Restaurants, Categories, Food_Log

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['dish_name', 'description', 'notes', 'food_image_url', 'price'] 
        
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'restaurant_name', 'restaurant_address', 'website_url']        
        
class CategorySerializer(serializers.ModelSerializer):
    """JSON Serializer for categories"""
    class Meta:
        model = Categories
        fields = ['category']

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
    