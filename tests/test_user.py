from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from culinary_explorer_api.models import User

class UserTests(TestCase):
    def setUp(self):
        """Data set up for the tests"""
        self.user_data = User.objects.create(
          first_name = "John",
          last_name = "Doe",
          email_address = "johnD@example.com",
          profile_image_url = "https://shorturl.at/iJM42",
          uid = "2321skm3lsl3ms3sas3fdfmasd32sa" 
        )

    def test_register_user(self):
        """Test user registration"""
        url = "/register"

        user_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email_address": "JaneD@example.com",
            "profile_image_url": "https://shorturl.at/iJM42",
            "uid": "sdwe24fr31qsddwqqe213124fqsd"
        }

        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, 200)
            
    def test_check_user_valid_uid(self):
        """Check if user exists"""
        url = "/checkuser"

        # self.client check the firs object of my table user
        response = self.client.post(url, {'uid': '12345'}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_check_user_invalid_uid(self):
        """Check if user exists"""
        url = "/checkuser"
        response = self.client.post(url, {'uid': 'invaliduid'}, format='json')
        self.assertFalse(response.data['valid'])
