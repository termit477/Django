from django.core.management.base import  BaseCommand
from homework_2.models import Client


class Command(BaseCommand):
    help = 'Delete client by ID'

    def add_arguments(self, parser, *args, **kwargs):
        parser.add_argument('id', type=int, help='Client ID')

    def handle (self, *args, **kwargs):
        id = kwargs.get('id')
        client = Client.objects.filter(pk=id).first()
        client.delete()
        self.stdout.write(self.style.ERROR(f'Deleted client: {client}'))
