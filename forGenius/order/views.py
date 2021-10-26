from django.shortcuts import render
from user.auth import token_to_email
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from user.errors import InputError
from product.errors import ProductIdError
from order.errors import EmptyCartError
import json
import order.cart as cart
import order.order as order
import jwt as jwt

# Create your views here.

def add_to_cart(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data['token']
            product_id = data['product_id']
            quantity = data['quantity']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            email = token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            cart.add_to_cart(email, product_id, quantity)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def view_cart(request):
    response = HttpResponse()
    if request.method == "GET":
        # try:
        #     data = json.loads(request.body)
        # except json.JSONDecodeError:
        #     response.status_code = 441
        #     response.content = 'json.JSONDecodeError'
        #     return response
        # try:
        token = request.GET.get("token")
        # except KeyError:
        #     response.status_code = 442
        #     response.content = 'KeyError'
        #     return response

        if token is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        try:
            email = token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            data = cart.view_cart(email)
        except InputError as e:
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

def create_order(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data['token']
            name = data['name']
            address = data['address']
            phone_number = data['phone_number']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            email = token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            order_id = order.create_order(email, name, address, phone_number)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except EmptyCartError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        data = order.view_order(email, order_id)
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

def view_order(request):
    response = HttpResponse()
    if request.method == "GET":
        token = request.GET.get("token")
        if token is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        order_id = request.GET.get("order_id")
        if order_id is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        try:
            email = token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            data = order.view_order(email, order_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except EmptyCartError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

def pay_order(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data['token']
            order_id = data['order_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            email = token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            order.pay_order(email, order_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response