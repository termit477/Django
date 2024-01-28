from django.urls import path
from .views import client, product, order, order_filter, client_add, product_add, order_add, product_image_add

urlpatterns = [
    path('clients/', client, name='client'),
    path('client_add/', client_add, name='client_add'),
    path('products/', product, name='product'),
    path('product_add/', product_add, name='product_add'),
    path('product_image/', product_image_add, name='product_image_add'),
    path('orders/', order, name='order'),
    path('order_add/', order_add, name='order_add'),
    path('orders/<int:client_id>/<int:days_ago>', order_filter, name='order_filter'),
]