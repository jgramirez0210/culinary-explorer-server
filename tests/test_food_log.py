from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from culinary_explorer_api.models import Food_Log, Categories, Restaurants, Dish, User

class TestFoodLog(APITestCase):
    
    fixtures = ['food_log.json', 'restaurants.json', 'dish.json', 'categories.json', 'users.json']

    def setUp(self):
        """Data set up for the tests"""
        self.category = Categories.objects.first()
        self.restaurants = Restaurants.objects.first()
        self.dish = Dish.objects.first()
        self.users = User.objects.first()
        self.food_log = Food_Log.objects.first()
        self.detail_url = reverse('food_log-detail', kwargs={'pk': self.food_log.pk})   
        self.list_url = reverse('food_log-list')

    def test_single_food_log(self):
        """Get single food log test"""
        response = self.client.get(self.detail_url)    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_list_all_food_log(self):
        """Get all food log tests"""
        response = self.client.get(self.list_url)
        all_food_log = Food_Log.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_food_log(self):
        """Create a food log"""
        url = reverse('food_log-list')
        food_log_payload = {
            'restaurant_id': '2',
            'dish_id': '2',
            'category_ids': [2],
            'uid': 'sd1wewd1241a231e12e'
        }
        response = self.client.post(url, food_log_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
    def test_update_food_log(self):
        """Test changing a food log entry"""
        update_entry = {
            'restaurant_id': '2',
            'dish_id': '2',
            'category_ids': [2],
            'uid': '213s'
        }
        response = self.client.put(self.detail_url, update_entry, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)