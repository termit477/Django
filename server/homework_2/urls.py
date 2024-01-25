from django.urls import path
from .views import client, product, order, order_filter

urlpatterns = [
    path('clients/', client, name='client'),
    path('products/', product, name='product'),
    path('orders/', order, name='order'),
    path('orders/<int:client_id>/<int:days_ago>', order_filter, name='order_filter'),
]