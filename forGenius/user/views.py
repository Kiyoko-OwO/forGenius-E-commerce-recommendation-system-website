from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from user.errors import InputError
import json
import user.auth as auth
import user.address as address

# Create your views here.
def register(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            email = data["email"]
            name = data["name"]
            password = data["password"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            token = data["token"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            token = data["token"]
            old_password = data["old_password"]
            new_password = data["new_password"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            email = data["email"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            reset_code = data["reset_code"]
            new_password = data["new_password"]
        except KeyError:
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
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            name = data['name']
            address = data['address']
            phone_number = data['phone_number']
        except KeyError:
            response.status_code = 400
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            address.add_address_book(email, name, address, phone_number)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

def view_address_book(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
        except KeyError:
            response.status_code = 400
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = address.view_address_book(email)
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
        print(jsons)
        return JsonResponse(jsons)
    response.status_code = 405
    return response


def delete_address_book(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 400
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            address_id = data['address_id']
        except KeyError:
            response.status_code = 400
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            address.delete_address_book(email, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response



def test():
    response = HttpResponse()
    data = {
        '11':'11',
        '11':'11',
    }
    meta = {'msg' : '', 'status': 200}
    json = [data, meta]
    return JsonResponse(meta)