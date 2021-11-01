from product.models import Product, Features
from product.errors import ProductIdError
from user.models import Admin
from datetime import datetime, timedelta

ADMIN_EMAIL = '3900forgenius@gmail.com'


def get_Admin():
    return Admin.objects.get()

def product_userView(product_id):
    try:
        product_query = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    delivery_date = datetime.now() + timedelta(days=product_query.delivery_date)

    info = {
            "name" : product_query.name,
            "description" : product_query.description,
            "warranty" : product_query.warranty,
            "delivery_date" : delivery_date.strftime("%Y-%m-%d"),
            "price" : product_query.price,
            "picture" : product_query.picture
        } 
    return info

def admin_add_product(name, description, warranty, delivery_date, price, picture):    
    reg = Product(admin_email=get_Admin(), name=name, description=description, warranty=warranty, delivery_date=delivery_date, price=price, picture=picture)
    reg.save()

def admin_edit_product(product_id, name, description, warranty, delivery_date, price, picture):    
    try:
        reg = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")
    reg.name = name
    reg.description = description
    reg.warranty = warranty
    reg.delivery_date = delivery_date
    reg.price = price
    reg.picture = picture
    reg.save()

def admin_delete_product(product_id):    
    try:
        reg = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")
    reg.delete()
    
def admin_products_all():
    try:        
        books = Product.objects.all()
    except:
        pass
    info_str = "product_details"
    data = { info_str : []}
    for book in books:
        info = {
            "product_id" : book.product_id,
            "name" : book.name,
            "warranty" : book.warranty,
            "description" : book.description,
            "delivery_date" : book.delivery_date,
            "sales_data" : book.sales_data,
            "price" : book.price,
            "picture" : book.picture
        } 
        data[info_str].append(info)
    return data