from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('user/view/', view_product_user, name='view_product_user'),
]
