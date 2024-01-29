from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .form import ClientForm, ProductForm, OrderForm, ImageProductForm
from .models import Client, Product, Order, ImageProduct


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


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name,
                            email=email,
                            password=password,
                            phone=phone,
                            address=address)
            client.save()
            message = 'Клиент сохранен'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'form_add.html', {'form': form, 'message': message})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            lot = form.cleaned_data['lot']
            product = Product(name=name,
                              price=price,
                              description=description,
                              lot=lot)
            product.save()
            message = 'Продукт сохранен'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'form_add.html', {'form': form, 'message': message})


def product_image_add(request):
    if request.method == 'POST':
        form = ImageProductForm(request.POST, request.FILES)
        message = 'Ошибка в загрузке картинки'
        if form.is_valid():
            product = form.cleaned_data['product']
            image = form.cleaned_data['image']
            imageProduct = ImageProduct(product=product,
                                        image=image)
            imageProduct.save()
            message = 'Картинка сохранена'
    else:
        form = ImageProductForm()
        message = 'Заполните форму'
    return render(request, 'form_add.html', {'form': form, 'message': message})


def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            order = Order(customer=customer)
            order.product = product
            order.total_order = float(product.price * product.lot)

            order.save()
            message = 'Заказ сохранен'
    else:
        form = OrderForm()
        message = 'Заполните форму'
    return render(request, 'form_add.html', {'form': form, 'message': message})
