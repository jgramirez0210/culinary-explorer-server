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
        try:
            category = Categories.objects.get(pk=pk)
            serializer = CategoriesSerializer(category)
            return Response(serializer.data)
        except Categories.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        """Handle GET requests to get all categories
        
        Returns:
            Response -- JSON serialized list of categories
        """
        try:
            categories = Categories.objects.all()
            if not categories.exists():
                return Response({'message': 'Categories not found.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CategoriesSerializer(categories, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request):
        """Handle Create Requests for categories"""
        try:
            new_category = Categories()
            new_category.category = request.data["category"]
            new_category.save()
            serializer = CategoriesSerializer(new_category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, pk):
        """Handles the delete functionality"""
        try:
            category = Categories.objects.get(pk=pk)
            category.delete()
            return Response('The Category was deleted', status=status.HTTP_204_NO_CONTENT)
        except Categories.DoesNotExist:
            return Response({'message': 'No category found to delete'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)