from order.errors import EmptyCartError, EmptyOrderError
from order.models import Order, Cart
from product.models import Product
from product.errors import ProductIdError
from user.models import User
from user.errors import InputError
import time
import datetime

def create_order(email, name, address_line, post_code, suburb, state, country, phone_number):
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    cart = Cart.objects.filter(user_email=user_email)
    if len(cart) == 0:
        raise EmptyCartError("Cart is empty")

    order_id = int(round(time.time() * 1000))

    for item in cart:
        try:
            product_id = Product.objects.get(pk=item.product_id.product_id)
        except Product.DoesNotExist:
            raise ProductIdError("This product does not exist")

        Order(order_id=order_id, user_email=user_email,
              product_id=item.product_id.product_id, 
              product_name=item.product_id.name,
              quantity=item.quantity, price=item.product_id.price,
              name=name, address_line=address_line, post_code=post_code, 
              suburb=suburb, state=state, country=country, phone_number=phone_number).save()
    cart.delete()
    return order_id

def view_order(email, order_id):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    order = Order.objects.filter(order_id=order_id, user_email=user_email)

    if len(order) == 0:
        raise EmptyOrderError("No order exists")
    
    for temp in order:
        data = {"order_id": order_id,
                "item" : [], 
                "total": 0,
                "name": temp.name,
                "address_line" : temp.address_line,
                "post_code": temp.post_code,
                "suburb": temp.suburb,
                "state": temp.state,
                "country": temp.country,
                "phone_number": temp.phone_number,
                "order_date": temp.date_time.strftime("%Y-%m-%d"),
                "paid": temp.paid,
                }
        break
    
    total = 0
    for item in order:
        info = {
            "product_id" : item.product_id,
            "name" : item.product_name,
            "price" : round(float(item.price), 2),
            "quantity" : item.quantity,
            "total_price": round(float(item.price), 2) * item.quantity
        } 
        total += round(float(item.price), 2) * item.quantity
        data["item"].append(info)
    
    data["total"] = total
    return data

def pay_order(email, order_id):
    # check user authorization (potential attack: one user pay another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    order = Order.objects.filter(order_id=order_id, user_email=user_email)

    if len(order) == 0:
        raise EmptyOrderError("No order exists")

    for item in order:
        if item.paid == False:
            products = Product.objects.filter(product_id=item.product_id)
            if len(products) != 0:
                for product in products:
                    product.sales_data += item.quantity
            item.paid = True
            item.save()

def view_all_order(email):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    user_order = Order.objects.filter(user_email=user_email)
    if len(user_order) == 0:
        raise EmptyOrderError("No order exists")
    
    order_ids = []

    for temp in user_order:
        if order_ids.count(temp.order_id) == 0:
            order_ids.append(temp.order_id)

    order_list = {"order_list": []}

    for curr_id in order_ids:
        order = Order.objects.filter(order_id=curr_id, user_email=user_email)

        data = {"order_id": curr_id,
                "item" : [], 
                "total": 0,
                "name": "",
                "address_line" : "",
                "post_code": "",
                "suburb": "",
                "state": "",
                "country": "",
                "phone_number": "",
                "order_date": "",
                "paid": "",
                }
    
        total = 0
        for item in order:
            info = {
                "product_id" : item.product_id,
                "name" : item.product_name,
                "price" : round(float(item.price), 2),
                "quantity" : item.quantity,
                "total_price": item.price * item.quantity
            } 
            if total == 0:
                data['name'] = item.name
                data['address_line'] = item.address_line
                data['post_code'] = item.post_code
                data['suburb'] = item.suburb
                data['state'] = item.state
                data['country'] = item.country
                data['phone_number'] = item.phone_number
                data['order_date'] = item.date_time.strftime("%Y-%m-%d")
                data['paid'] = item.paid

            total += round(float(item.price), 2) * item.quantity
            data["item"].append(info)
    
        data["total"] = total
        order_list["order_list"].append(data)
    return order_list
