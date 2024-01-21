from django.http import HttpResponse
from .models import Client, Product, Order


def client(request):
    clients = Client.objects.all()
    res = '<br>'.join(str(client) for client in clients)
    return HttpResponse(res)


def product(request):
    products = Product.objects.all()
    res = '<br>'.join(str(product) for product in products)
    return HttpResponse(res)


def order(request):
    orders = Order.objects.all()
    res = '<br>'.join(str(order) for order in orders)
    return HttpResponse(res)
