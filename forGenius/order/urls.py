from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]
