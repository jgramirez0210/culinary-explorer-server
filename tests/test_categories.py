from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from culinary_explorer_api.models import Categories

class TestCategories(APITestCase):
    
    fixtures = ['categories.json']
    
    def setUp(self):
        """Data set up for the tests"""
        self.category = Categories.objects.first()
        self.detail_url = reverse('categories-detail', kwargs={'pk': self.category.pk})   
        self.list_url = reverse('categories-list')

    def test_single_category(self):
        """Get Single Category Test"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_list_all_categories(self):
        """Get All Categories Test"""
        response = self.client.get(self.list_url)
        all_categories = Categories.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_category(self):
        """Create a Category Test"""
        url = reverse('categories-list')
        categories_payload = {'category': 'Asiann'}
        response = self.client.post(url, categories_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(self.list_url)

    def test_delete_category(self):
        """Test deleting a category"""
        category = Categories.objects.first()
        url = f'/categories/{category.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)