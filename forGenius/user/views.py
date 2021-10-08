from json import encoder
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from user.errors import InputError
import user.auth as auth
import user.address as address

# Create your views here.
def register(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            email = request.GET['email']
            name = request.GET['name']
            password = request.GET['password']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        try:
            auth.auth_register(email, name, password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def login(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            email = request.GET['email']
            password = request.GET['password']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        try:
            auth.auth_login(email, password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def logout(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            token = request.GET['token']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        auth.auth_logout(token)
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def change_password(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            token = request.GET['token']
            old_password = request.GET['old_password']
            new_password = request.GET['new_password']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        try:
            auth.auth_change_password(token, old_password, new_password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def send_reset_code(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            email = request.GET['email']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        try:
            auth.auth_send_reset_code(email)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def reset_password(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            reset_code = request.GET['reset_code']
            new_password = request.GET['new_password']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        try:
            auth.auth_reset_password(reset_code, new_password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def add_address_book(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            #token = request.GET['token']
            email = request.GET['email']
            user_address = request.GET['address']
            phone_number = request.GET['phone_number']
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        #except InputError: # invalid error
        #    pass             
        address.add_address_book(email, user_address, phone_number)
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def view_address_book(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            token = request.GET['token']
            email = auth.token_to_email(token)
        except MultiValueDictKeyError:
            response.status_code = 400
            return response
        #except InputError: # invalid error
        #    pass             
        address.view_address_book(email)
        response.status_code = 200
        return response
    response.status_code = 405
    return response
