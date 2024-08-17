from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from culinary_explorer_api.models import Categories

class CategoriesTests(TestCase):
    def setUp(self):
        """Data set up for the tests"""
        self.client = APIClient()