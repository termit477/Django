from django.core.management.base import BaseCommand
from homework_2.models import Client


class Command(BaseCommand):
    help = 'Get client by ID'

    def add_arguments(self, parser, *args, **kwargs):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.filter(pk=id).first()
        self.stdout.write(self.style.ERROR(f'Client with ID [{id}]: {client}'))
