from django.core.management.base import BaseCommand
from homework_2.models import Client


class Command(BaseCommand):
    help = 'Get all clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(self.style.ERROR(f'Clients: {clients}'))
