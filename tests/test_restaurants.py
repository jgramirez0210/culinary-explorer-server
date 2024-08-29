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
        """Get single restaurants"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
    
    def test_list_all_restaurants(self):
        """Get all restaurants"""
        response = self.client.get(self.list_url)
        all_restaurants = Restaurants.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_restaurant(self):
        """Create new restaurant"""
        url =reverse('restaurants-list')
        restaurants_payload = {
            'restaurant_name' : 'Taco Mammmmmmacita',
            'restaurant_address' : '1234 6th Ave N, Nashville, TN 37208',
            'website_url' : 'http://www.tacomamacitagermantown.com/',
        }
        response = self.client.post(url, restaurants_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    
        
    def test_update_restaurant(self):
        """Test changing a restaurant"""
        update_restaurants = {
            'restaurant_name' : 'Taco Mamacita',
            'restaurant_address' : '1234 6th Ave N, Nashville, TN 37208',
            'website_url' : 'http://www.tacomamacitagermantown.com/',            
        }
        response = self.client.put(self.detail_url, update_restaurants, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_restaurant(self):
        """Test to delete a restaurant"""
        url = reverse('restaurants-detail', kwargs={'pk': self.restaurants.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
                       