from random import randint, choice
from typing import Any
from django.core.management.base import BaseCommand
from homework_2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create data'

    def handle(self, *args: Any, **kwargs: Any):
        client_list = []
        product_list = []

        for i in range(1, 11):
            client = Client(name=f'Name {i}',
                            email=f'{i}@mail.ru',
                            password=f'Password{i}',
                            phone=f'7-123-456-78-{i}',
                            address=f'Address{i}')

            client_list.append(client)
            self.stdout.write(f'{client}')
            client.save()

        for i in range(1, 21):
            product = Product(name=f'Product {i}',
                              price=float(randint(10, 1000)),
                              description=f'lorem to create{i}',
                              lot=randint(1, 10))
            product_list.append(product)
            self.stdout.write(f'{product}')
            product.save()

        for i in range(1, 21):
            order = Order(customer=choice(client_list))
            for j in range(0, 10):
                if choice([0, 1]) == 1:
                    total = order.total_order + float(product_list[j].price * product_list[j].lot)
                    order = Order(customer=choice(client_list),
                                  product=product_list[j],
                                  total_order=total)
                    order.save()
