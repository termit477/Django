from django import forms
from .models import Client, Product, Order, ImageProduct


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'password', 'phone', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'lot']


class ImageProductForm(forms.ModelForm):
    class Meta:
        model = ImageProduct
        fields = ['product', 'image']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product']
