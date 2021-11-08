from product.models import Product, Features
from product.errors import ProductIdError
from product.products import get_product_features

def public_recommendation():
    top_selling_products = Product.objects.order_by('-sales_data')
    data = {
        "product_number": 0,
        "products": [],
    }
    product_number = 0
    for product in top_selling_products:
        info = {
                "product_id" : product.product_id,
                "name" : product.name,
                "description" : product.description,
                "price" : round(float(product.price), 2),
                "picture" : product.picture,
                "features" : get_product_features(product.product_id),
                "sales_data" : product.sales_data
            }
        data["products"].append(info)
        product_number += 1
    data["product_number"] = product_number
    return data
