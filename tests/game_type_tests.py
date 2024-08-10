from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from levelupapi.models import Game_Type, Gamer
from levelupapi.views.game_type import GameTypeSerializer


class GameTypeTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['game_types']
    
    def setUp(self):
        # Grab the first Gamer object from the database
        self.game_type = Game_Type.objects.first()

        
    def test_get_game_type(self):
        """Get game_type Test"""
        # Grab a game_type object from the database
        game_type = Game_Type.objects.first()

        # Use the ID of the game_type object for the URL
        url = f'/gametypes/{game_type.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # Run the game_type through the serializer that's being used in view
        expected = GameTypeSerializer(game_type)

        # Assert that the response matches the expected return data
        self.assertEqual(expected.data, response.data)
        
    def test_list_game_type(self):
        """Test list game types"""
        url = '/gametypes'  # This URL should likely be '/gametypes' instead of '/gamers'
    
        response = self.client.get(url)
        
        # Get all the game types in the database and serialize them to get the expected output
        all_game_types = Game_Type.objects.all()
        expected = GameTypeSerializer(all_game_types, many=True)  # Corrected variable name here
    
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)