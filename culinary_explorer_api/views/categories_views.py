from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from culinary_explorer_api.models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    """JSON Serializer for categories"""
    class Meta:
        model = Categories
        fields = ['id', 'category']


class CategoriesView(ViewSet):
    """Culinary Explorer Categories View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        category = Categories.objects.filter(pk=pk).first()
        
        if category is None:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)