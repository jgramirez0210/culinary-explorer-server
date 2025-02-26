from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from culinary_explorer_api.models import Restaurants

class Command(BaseCommand):
    help = 'Update uid field for existing restaurants'

    def handle(self, *args, **kwargs):
        try:
            default_user = User.objects.get(username='default_user')
            Restaurants.objects.all().update(uid=default_user)
            self.stdout.write(self.style.SUCCESS('Successfully updated uid field for existing restaurants'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Default user does not exist'))