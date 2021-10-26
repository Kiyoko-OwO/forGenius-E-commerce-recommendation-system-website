from order.errors import EmptyCartError
from order.models import Order, Cart
from product.models import Product
from user.models import User
from user.errors import InputError
import time

def create_order(email, name, address, phone_number):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    cart = Cart.objects.filter(user_email=user_email)
    if len(cart) == 0:
        raise EmptyCartError("Cart is empty")

    order_id = int(round(time.time() * 1000))

    for item in cart:
        # product_id = Product.objects.get(pk=item.product_id)
        Order(order_id=order_id, product_id=item.product_id,
              user_email=user_email, quantity=item.quantity, price=item.product_id.price,
              name=name, address=address, phone_number=phone_number).save()
    cart.delete()
    return order_id

def view_order(email, order_id):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    order = Order.objects.filter(order_id=order_id)
    if len(order) == 0:
        raise InputError('Order not exist')
    
    for temp in order:
        data = {"order_id": order_id,
                "item" : [], 
                "total": 0,
                "name": temp.name,
                "address": temp.address,
                "phone_number": temp.phone_number,
                "paid": temp.paid,
                }
        break
    
    total = 0
    for item in order:
        info = {
            "product_id" : item.product_id.product_id,
            "name" : item.product_id.name,
            "price" : item.price,
            "quantity" : item.quantity,
            "total_price": item.price * item.quantity
        } 
        total += item.price * item.quantity
        data["item"].append(info)
    
    data["total"] = total
    return data

def pay_order(email, order_id):
    # check user authorization (potential attack: one user pay another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    order = Order.objects.filter(order_id=order_id)
    if len(order) == 0:
        raise InputError('Order not exist')

    for item in order:
        item.paid = True
        item.save()
