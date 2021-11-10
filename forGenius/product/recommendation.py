from product.models import Product, Features
from product.products import get_product_features
from user.models import User, Interest
from user.errors import InputError
import random

# return the recommendation if the user is logout(guest mode)
def public_recommendation():

    # sort the product with selling data
    top_selling_products = Product.objects.order_by('-sales_data')
    data = {
        "product_number": 0,
        "products": [],
    }
    product_number = 0

    # output the relevant selling products
    for product in top_selling_products:
        info = {
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": round(float(product.price), 2),
            "picture": product.picture,
            "features": get_product_features(product.product_id),
            "sales_data": product.sales_data
        }
        data["products"].append(info)
        product_number += 1

    data["product_number"] = product_number
    # output the products with ordered number
    return pick_products(data, 6)

# return the recommendation if the user is logged (user mode)
def private_recommendation(email):
    # search the user email to find its interest
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    data = public_recommendation()

    # put relevent products with interests in the recommendation array
    interests = Interest.objects.filter(user_email=user_email)
    for interest in interests:
        for feature in Features.objects.filter(feature=interest.interests):
            product = feature.product_id
            info = {
                "product_id": product.product_id,
                "name": product.name,
                "description": product.description,
                "price": round(float(product.price), 2),
                "picture": product.picture,
                "features": get_product_features(product.product_id),
                "sales_data": product.sales_data
            }
            if info not in data["products"]:
                data["products"].append(info)
                data["product_number"] += 1
    # sort the products with selling datas
    data["products"] = sorted(data["products"], key=lambda x: -x["sales_data"])
    return pick_products(data, 6)

# pick selected number of the products from the recommendation lists
def pick_products(product_list, num):
    if product_list["product_number"] <= num:
        return product_list
    # use random algorithms to select
    samples = random.sample(product_list["products"], num)
    data = {
        "product_number": num,
        "products": samples,
    }
    return data

# balance recommendation lists to selected number of the products
def balance_products(product_list, num):
    if len(product_list) <= num:
        return product_list
    # use random algorithms to select
    to_delete = random.sample(range(product_list), len(product_list) - num)
    return [x for i, x in enumerate(product_list) if not i in to_delete]
