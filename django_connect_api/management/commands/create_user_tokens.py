from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Creates auth tokens for all users'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created token for user: {user.username} - Token: {token.key}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Token already exists for user: {user.username} - Token: {token.key}'))

        self.stdout.write(self.style.SUCCESS('Finished creating tokens'))
