from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from .models import Client, Product, Order


def client(request):
    clients = Client.objects.all()
    context = {
        'title': 'Клиенты',
        'result': clients
    }
    return render(request, 'clients.html', context=context)


def product(request):
    products = Product.objects.all()
    context = {
        'title': 'Продукты',
        'result': products
    }
    return render(request, 'products.html', context=context)


def order(request):
    orders = Order.objects.all()
    context = {
        'title': 'Заказы',
        'result': orders
    }
    return render(request, 'orders.html', context=context)




def order_filter(request, client_id, days_ago):
    products_filter = []
    time_now = datetime.now()
    time_before = time_now - timedelta(days=days_ago)
    client = Client.objects.filter(pk=client_id).first()
    print(client)
    orders = Order.objects.filter(
        customer=client,
        date__range=(time_before, time_now)).all()
    for order in orders:
        products = order.product.all()
        for product in products:
            if product not in products_filter:
                products_filter.append(product)
    context = {
        'days_ago': days_ago,
        'result': products_filter
    }
    return render(request, 'orders_filter.html', context=context)



