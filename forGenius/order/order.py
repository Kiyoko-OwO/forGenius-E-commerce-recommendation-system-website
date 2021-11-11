from order.errors import EmptyCartError, EmptyOrderError
from order.models import Order, Cart
from product.models import Product
from product.errors import ProductIdError
from user.models import User
from user.errors import InputError
import time
import datetime
import user.email_robot as email_robot

# the function to create order from the cart
def create_order(email, name, address_line, post_code, suburb, state, country, phone_number):
    # if the user does not exist, raise error
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # get user's cart, if it is empty, raise error
    cart = Cart.objects.filter(user_email=user_email)
    if len(cart) == 0:
        raise EmptyCartError("Cart is empty")

    # create the order id based the time
    order_id = int(round(time.time() * 1000))

    # get all items fron the cart
    for item in cart:
        # if the product does not exist, raise error
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

# the function to view the order detail information 
def view_order(email, order_id):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # get the order with this user email and order id 
    order = Order.objects.filter(order_id=order_id, user_email=user_email)

    if len(order) == 0:
        raise EmptyOrderError("No order exists")

    # Put all of the detail information of this order to data
    for temp in order:
        data = {"order_id": order_id,
                "item": [],
                "total": 0,
                "name": temp.name,
                "address_line": temp.address_line,
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
    
    # put the items in order to data
    for item in order:
        product_pic = ""
        try:
            product_pic = Product.objects.get(pk=item.product_id).picture
        except:
            product_pic = "https://i.imgur.com/xzuy857.png"

        info = {
            "product_id": item.product_id,
            "name": item.product_name,
            "price": round(float(item.price), 2),
            "quantity": item.quantity,
            "picture": product_pic,
            "total_price": round(float(item.price), 2) * item.quantity
        }
        total += round(float(item.price), 2) * item.quantity
        data["item"].append(info)

    data["total"] = round(total, 2)
    return data

# the function to pay for the order
def pay_order(email, order_id):
    # check user authorization (potential attack: one user pay another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    
    # get the order with this user email and order id 
    order = Order.objects.filter(order_id=order_id, user_email=user_email)

    if len(order) == 0:
        raise EmptyOrderError("No order exists")

    # pay the order and add product sales data
    for item in order:
        if item.paid == False:
            products = Product.objects.filter(product_id=item.product_id)
            if len(products) != 0:
                for product in products:
                    product.sales_data += item.quantity
                    product.save()
            item.paid = True
            item.save()

# the function to view all of the user's order history
def view_all_order(email):
    # check user authorization (potential attack: one user view another user's order)
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

     # get the order with this user email 
    user_order = Order.objects.filter(user_email=user_email)
    if len(user_order) == 0:
        raise EmptyOrderError("No order exists")

    order_ids = []
    
    # get all order id from dababase
    for temp in user_order:
        if order_ids.count(temp.order_id) == 0:
            order_ids.append(temp.order_id)

    order_list = {"order_list": []}

    # get all details of the order ids
    for curr_id in order_ids:
        order = Order.objects.filter(order_id=curr_id, user_email=user_email)

        data = {"order_id": curr_id,
                "item": [],
                "total": 0,
                "name": "",
                "address_line": "",
                "post_code": "",
                "suburb": "",
                "state": "",
                "country": "",
                "phone_number": "",
                "order_date": "",
                "paid": "",
                }

        total = 0
        
        # put the items in order to order's data
        for item in order:
            product_pic = ""
            try:
                product_pic = Product.objects.get(pk=item.product_id).picture
            except:
                product_pic = "https://i.imgur.com/xzuy857.png"
            info = {
                "product_id": item.product_id,
                "name": item.product_name,
                "price": round(float(item.price), 2),
                "quantity": item.quantity,
                "picture": product_pic,
                "total_price": round(float(item.price), 2) * item.quantity
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

        data["total"] = round(total, 2)
        order_list["order_list"].append(data)
    return order_list

# the function to share the order details to the to email
def share_order(email, order_id, to_email, receiver):
    # get order's detail
    data = view_order(email, order_id)
    email_query = User.objects.get(pk=email)
    
    # get the order's detail data to text message
    message = "order id" + " : " + \
        str(data["order_id"]) + "\n" + "items" + " :\n"
    for i in data["item"]:
        message = message + "       " + "product id" + \
            " : " + str(i["product_id"]) + "\n"
        message = message + "       " + "name" + " : " + str(i["name"]) + "\n"
        message = message + "       " + "unit price" + \
            " : " + str(i["price"]) + "\n"
        message = message + "       " + "quantity" + \
            " : " + str(i["quantity"]) + "\n"
        message = message + "       " + "price" + \
            " : " + str(i["total_price"]) + "\n\n"

    message = message + "total price" + " : " + str(data["total"]) + "\n"
    message = message + "recipient" + " : " + str(data["name"]) + "\n"
    message = message + "address" + " : " + str(data["address_line"]) + "\n"
    message = message + "post code" + " : " + str(data["post_code"]) + "\n"
    message = message + "suburb" + " : " + str(data["suburb"]) + "\n"
    message = message + "state" + " : " + str(data["state"]) + "\n"
    message = message + "country" + " : " + str(data["country"]) + "\n"
    message = message + "phone number" + \
        " : " + str(data["phone_number"]) + "\n"
    message = message + "order date" + " : " + str(data["order_date"]) + "\n"
    message = message + "paid" + " : " + str(data["paid"]) + "\n"

    # send the text message to receiver's email
    email_robot.send_email_share(
        email_query.user_name, to_email, message, receiver)
