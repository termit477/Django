# Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.

# *Допишите несколько функций CRUD для работы с
# моделями по желанию. Что по вашему мнению актуально в
# такой базе данных.

from django.db import models

# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, ' \
               f'email: {self.email}'

# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    lot = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.name}, ' \
               f'price: {self.price}'


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары, входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_order = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
