from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a default user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='default_user').exists():
            User.objects.create_user(username='default_user', password='default_password')
            self.stdout.write(self.style.SUCCESS('Successfully created default user'))
        else:
            self.stdout.write(self.style.SUCCESS('Default user already exists'))