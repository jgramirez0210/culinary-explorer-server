from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from levelupapi.models import Game, Gamer
from levelupapi.views.GamerView import GamerSerializer


class GamerTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['gamers']
    
    def setUp(self):
        # Grab the first Gamer object from the database
        self.gamer = Gamer.objects.first()

    def test_create_gamer(self):
        """Create gamer test"""
        url = "/gamers"

        # Define the Gamer properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        gamer = {
            "uid": "{The uid of the first gamer object in your fixtures}",
            "bio": "A test Bio",
        }

        response = self.client.post(url, gamer, format='json')
        
        # Get the last gamer added to the database, it should be the one just created
        new_gamer = Gamer.objects.last()

        # Since the create method should return the serialized version of the newly created gamer,
        # Use the serializer you're using in the create method to serialize the "new_gamer"
        # Depending on your code this might be different
        expected = GamerSerializer(new_gamer)

        # Now we can test that the expected ouput matches what was actually returned
        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        self.assertEqual(expected.data, response.data)
        
    def test_get_gamer(self):
        """Get Gamer Test
        """
        # Grab a gamer object from the database
        gamer = Gamer.objects.first()

        url = f'/gamers/{gamer.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # Like before, run the gamer through the serializer that's being used in view
        expected = GamerSerializer(gamer)

        # Assert that the response matches the expected return data
        self.assertEqual(expected.data, response.data)
        
    def test_list_gamers(self):
        """Test list gamers"""
        url = '/gamers'

        response = self.client.get(url)
        
        # Get all the gamers in the database and serialize them to get the expected output
        all_gamers = Gamer.objects.all()
        expected = GamerSerializer(all_gamers, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)    
        
    def test_change_gamer(self):
        """test update gamer"""
        # Grab the first gamer in the database
        gamer = Gamer.objects.first()

        url = f'/gamers/{gamer.id}'

        updated_gamer = {
            "bio": f'{gamer.bio} updated',
        }

        response = self.client.put(url, updated_gamer, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the gamer object to reflect any changes in the database
        gamer.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_gamer['bio'], gamer.bio) 
        
    def test_delete_gamer(self):
        """Test delete gamer"""
        gamer = Gamer.objects.first()
    
        url = f'/gamers/{gamer.id}'
        response = self.client.delete(url)
    
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    
        # Test that it was deleted by trying to _get_ the gamer
        # The response should return a 404
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)