from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/view/', view_cart, name='view_cart'),
    path('create/', create_order, name='create_order'),
    path('view/', view_order, name='view_order'),
    path('pay/', pay_order, name='pay_order'),
]
