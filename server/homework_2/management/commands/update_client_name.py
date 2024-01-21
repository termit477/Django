from django.core.management.base import BaseCommand
from homework_2.models import Client


class Command(BaseCommand):
    help = 'Get client by ID'

    def add_arguments(self, parser, *args, **kwargs):
        parser.add_argument('id', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        name = kwargs['name']
        client = Client.objects.filter(pk=id).first()
        client.name = name
        client.save()
        self.stdout.write(self.style.ERROR(f'Client with ID rename: {client}'))
