from order.models import Order, Cart
from order.errors import CartProductError,EmptyCartError
from product.models import Product
from product.errors import ProductIdError
from user.models import User
from user.errors import InputError


def add_to_cart(email, product_id, quantity):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    try:
        user_cart = Cart.objects.get(user_email=user_email, product_id=product_id)
        user_cart.quantity = quantity + user_cart.quantity
        user_cart.save()
    except Cart.DoesNotExist:
        to_cart = Cart(user_email=user_email, product_id=product_id, quantity=quantity)
        to_cart.save()  

def view_cart(email):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    cart = Cart.objects.filter(user_email=user_email)
    data = {
            "cart" : [], 
            "total": 0
        }
    total = 0
    
    for item in cart:
        info = {
            "product_id" : item.product_id.product_id,
            "name" : item.product_id.name,
            "price" : item.product_id.price,
            "quantity" : item.quantity,
            "total_price": item.quantity * item.product_id.price
        } 
        total += item.quantity * item.product_id.price
        data["cart"].append(info)
    
    data["total"] = total
    return data



def edit_cart_product_quantity(email, product_id, quantity):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    try:
        user_cart = Cart.objects.get(user_email=user_email, product_id=product_id)
        user_cart.quantity = quantity
        user_cart.save()
    except Cart.DoesNotExist:
        raise CartProductError("This product does not exist in the cart")

def remove_cart_product(email, product_id):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    try:
        user_cart = Cart.objects.get(user_email=user_email, product_id=product_id)
        user_cart.delete()
    except Cart.DoesNotExist:
        raise CartProductError("This product does not exist in the cart")
