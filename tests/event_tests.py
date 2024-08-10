from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from levelupapi.models import Event, Gamer, Game
from levelupapi.views.EventView import EventViewSerializer
from django.test import TestCase
from django.urls import reverse
from levelupapi.models import Event
from django.utils import timezone
from datetime import datetime

class EventTests(APITestCase):
    fixtures = ['gamers', 'game_types', 'events', 'games']
  
    def setUp(self):
        # Assuming the fixtures are loaded and there's at least one Event available.
        self.event = Event.objects.first()
        self.url = reverse('event-detail', kwargs={'pk': self.event.pk})
        
    def test_create_event(self):
        """Create event test"""
        url = "/events"
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        event_payload = {
            "description": "Another Test Event",
            "date": current_date,
            "time": current_time, 
            "gameId": self.event.game.id,
            "organizerId": self.event.organizer.id,
        }
        response = self.client.post(url, event_payload, format='json')
        new_event = Event.objects.last()
        expected = EventViewSerializer(new_event)
        self.assertEqual(response.data['description'], event_payload['description'])
        
    def test_change_event(self):
        """test update event"""
        # Ensure there's an event to update
        if not Event.objects.exists():
            gamer = Gamer.objects.create_user(username='testuser', password='password123')
            game = Game.objects.create(name="Test Game", game_type_id=1, number_of_players=4, gamer=gamer)
            event = Event.objects.create(description="Initial Event", date="2023-01-01", time="12:00:00", game=game, organizer=gamer)
        else:
            event = Event.objects.first()

        self.client.force_authenticate(user=event.organizer)
        url = f'/events/{event.id}/'
        updated_event_payload = {
            "description": "Updated Test Event",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "gameId": event.game.id,
            "organizerId": event.organizer.id,
        }
        response = self.client.put(url, updated_event_payload, format='json')
        # Assert that the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_event(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_OK)
        # Corrected to assert on 'description' instead of 'name'
        self.assertEqual(response.data['description'], self.event.description)

    def test_list_events(self):
        """Test list events"""
        url = '/events'
        response = self.client.get(url)
        all_events = Event.objects.all()
        expected = EventViewSerializer(all_events, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)