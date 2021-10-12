from django.shortcuts import render
from user.auth import token_to_email
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from user.errors import InputError
from product.errors import ProductIdError
import json
import order.cart as cart
import jwt as jwt

# Create your views here.

def add_to_cart(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeErro'
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