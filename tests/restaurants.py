from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from culinary_explorer_api.models import Restaurants

class TestRestaurants(APITestCase):
    fixtures = ['restaurants.json']
    
    def setUp(self):
        """Data set up for restaurants tests"""
        self.restaurant = Restaurants.objects.first()
        self.detail_url = reverse('restaurants-detail', kwargs={'pk':self.restaurants.pk})
        self.list_url = reverse('restaurants-list')