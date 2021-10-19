from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/view/', view_cart, name='view_cart'),
]