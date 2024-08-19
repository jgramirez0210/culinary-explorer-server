from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from culinary_explorer_api.models import Categories

class TestCategories(APITestCase):
    
    fixtures = ['categories.json']
    
    def setUp(self):
        """Data set up for the tests"""
        self.category = Categories.objects.first()
        self.detail_url = reverse('categories-detail', kwargs={'pk': self.category.pk})   
        self.list_url = reverse('categories-list')
        print(f"Setup category: {self.category}")

    def test_category_setup(self):
        """Test to ensure setup is correct"""
        self.assertIsNotNone(self.category, "Setup category should not be None")
        self.assertTrue(hasattr(self.category, 'category'), "Setup category should have a 'category' attribute")
    
    def test_single_category(self):
        """Get Single Category Test"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_list_all_categories(self):
        """Get All Categories Test"""
        response = self.client.get(self.list_url)
        all_categories = Categories.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), all_categories.count())
