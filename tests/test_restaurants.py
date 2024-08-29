from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from culinary_explorer_api.models import Restaurants

class TestRestaurants(APITestCase):
    fixtures = ['restaurants.json']
    
    def setUp(self):
        """Data set up for restaurants tests"""
        self.restaurants = Restaurants.objects.first()
        self.detail_url = reverse('restaurants-detail', kwargs={'pk':self.restaurants.pk})
        self.list_url = reverse('restaurants-list')
        
    def test_single_restaurant(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    