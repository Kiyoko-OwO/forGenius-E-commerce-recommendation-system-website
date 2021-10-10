from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('view_product_user/', view_product_user, name='view_product_user'),
]
