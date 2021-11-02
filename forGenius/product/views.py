from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.http.response import JsonResponse
from product.errors import ProductIdError
from user.errors import InputError
import product.products as products
import user.auth as auth
import json

# Create your views here.
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def view_product_user(request):
 
    response = HttpResponse()
    if request.method == "GET":
        # try:
        #     data = json.loads(request.body)
        # except json.JSONDecodeError:
        #     response.status_code = 441
        #     response.content = 'json.JSONDecodeErro'
        #     return response
        
        
        product_id = request.GET.get("product_id")
        # except KeyError:
        #     response.status_code = 442
        #     response.content = "format is wrong"
        #     return response

        if product_id is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        try:
            data = products.product_userView(product_id)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        meta = {'msg' : 'OK', 'status': 200}
        jsons = {
            'data' : data,
            'meta' : meta
        }
        return JsonResponse(jsons)
    response.status_code = 405
    return response

def admin_add_product(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            name = data['name']
            description = data['description']
            warranty = data['warranty']
            delivery_date = data['delivery_date']
            price = data['price']
            picture = data['picture']
            if not isFloat(price) or float(price) <= 0:
                response.status_code = 443
                response.content = 'price is not float'
                return response
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_add_product(name, description, warranty, delivery_date, price, picture)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def admin_edit_product(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            name = data['name']
            description = data['description']
            warranty = data['warranty']
            delivery_date = data['delivery_date']
            price = data['price']
            product_id = data['product_id']
            picture = data['picture']
            if not isFloat(price) or float(price) <= 0:
                response.status_code = 443
                response.content = 'price is not float or price <= 0'
                return response
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_edit_product(product_id, name, description, warranty, delivery_date, price, picture)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response
        
def admin_delete_product(request):
    response = HttpResponse()
    if request.method == "DELETE":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            product_id = data['product_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            products.admin_delete_product(product_id)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response
        

def admin_products_all(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            pass
            #token = data["token"]
            #email = auth.token_to_email(token)
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_products_all()
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        meta = {'msg' : 'OK', 'status': 200}
        jsons = {
            'data' : data,
            'meta' : meta
        }
        return JsonResponse(jsons)
    response.status_code = 405
    return response
