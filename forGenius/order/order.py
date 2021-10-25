from order.errors import EmptyCartError
from order.models import Order, Cart
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
        Order(order_id=order_id, product_id=item.product_id.product_id,
              user_email=user_email, quantity=item.quantity, price=item.product_id.price,
              name=name, address=address, phone_number=phone_number).save()
    cart.delete()

def view_order(email, order_id):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    order = Order.objects.filter(order_id=order_id)
    if len(order) == 0:
        raise InputError('Order not exist')
    
    first_line = order[:1].get()
    data = {"order_id": order_id,
            "item" : [], 
            "total": 0,
            "name": first_line.name,
            "address": first_line.address,
            "phone_number": first_line.phone_number,
            "paid": first_line.paid,
            }
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
        data["order"].append(info)
    
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
