from order.models import Order, Cart
from product.models import Product
from user.models import User
from user.errors import InputError
from product.errors import ProductIdError


def add_to_cart(email, product_id, quantity):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    to_cart = Cart(user_email=user_email, product_id=product_id, quantity=quantity)
    to_cart.save()  

