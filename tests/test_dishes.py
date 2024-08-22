from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from culinary_explorer_api.models import Dish

class TestDishes(APITestCase):
    fixtures = 'dishes.json'
    
    def setUp(self):
        """Data set up for tests"""
        self.dish = Dish.object.first()
        self.detail_url = reverse('dish-detail', kwargs={'pk':self.food_log.pk})
        self.list_url = reverse('dish-list')
        
    def test_get_single_dish(self):
        """Get single dish test"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_list_all_dishes(self):
        """Get all dishes test"""
        response = self.client.get(self.list_url)
        all_dishes = Dish.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_dish(self):
        """Create Dish entry"""
        url = reverse('dish-list')
        dish_payload = {
            'dish_name' : 'Chicken Parmesanssss',
            'description' : 'Chicken Parmesan is a popular Italian-American dish consisting of breaded and fried chicken breasts topped with marinara sauce and melted mozzarella cheese.',
            'notes' : 'no dairy free cheese',
            'food_image_url' : 'https://shorturl.at/aTQIv',
            'price' : '22.99'
        }
        response = self.client.post(url, dish_payload, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_change_dish(self):
        """Update Dish Entry"""
        
        update_dish_payload = {
            'dish_name' : 'Chicken Parmesan',
            'description' : 'Chicken Parmesan is a popular Italian-American dish consisting of breaded and fried chicken breasts topped with marinara sauce and melted mozzarella cheese.',
            'notes' : 'no dairy free cheese',
            'food_image_url' : 'https://shorturl.at/aTQIv',
            'price' : '22.99'
        }
        response = self.client.put(self.url, update_dish_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_dish(self):
        """Test Delete Dish Entry"""
        url = reverse('dish-detail', kwargs={'pk' : self.dish.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)                       