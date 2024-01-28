from typing import Any
from django.core.management.base import BaseCommand
from homework_2.models import Client


class Command(BaseCommand):
    help = 'Create Client'

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        for i in range(1, 11):
            client = Client(name=f'Name {i}',
                            email=f'{i}@mail.ru',
                            password=f'Password{i}',
                            phone=f'7-123-456-78-{i}',
                            address=f'Address {i}')

            self.stdout.write(self.style.ERROR(f'{client}'))
            client.save()
