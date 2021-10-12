from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from user.errors import InputError
import json
import user.auth as auth
import user.address as address
import user.interest as interest
import jwt as jwt

ADMIN_EMAIL = '3900forgenius@gmail.com'

# Create your views here.
def register(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            email = data["email"]
            name = data["name"]
            password = data["password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        try:
            token = auth.auth_register(email, name, password)
            username = auth.token_to_username(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        data = {
            'token':token,
            'username':username,
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

def login(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        try:
            token = auth.auth_login(email, password)
            username = auth.token_to_username(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        data = {
            'token':token,
            'username':username,
        }
        if email == ADMIN_EMAIL:
            return HttpResponse(json.dumps(data), content_type="application/json", status=255)
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

def logout(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            old_password = data["old_password"]
            new_password = data["new_password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            email = data["email"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            reset_code = data["reset_code"]
            new_password = data["new_password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            name = data['name']
            address_name = data['address']
            phone_number = data['phone_number']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            address.add_address_book(email, name, address_name, phone_number)
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
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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
        return JsonResponse(jsons)
    response.status_code = 405
    return response


def delete_address_book(request):
    response = HttpResponse()
    if request.method == "DELETE":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            address_id = data['address_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
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

def edit_address_book(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            name = data['name']
            address_name = data['address']
            phone_number = data['phone_number']
            address_id = data['address_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = address.edit_address_book(email, name, address_name, phone_number, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

def address_book_detail(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            email = auth.token_to_email(token)
            address_id = data['address_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = address.address_book_detail(token, email, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response

# def test():
#     response = HttpResponse()
#     data = {
#         '11':'11',
#         '11':'11',
#     }
#     meta = {'msg' : '', 'status': 200}
#     json = [data, meta]
#     return JsonResponse(meta)



def add_user_interests(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            interest_list = data['interest']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        
        try:
            email = auth.token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            interest.user_interest(email, interest_list)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response
    response.status_code = 405
    return response



def add_user_interests(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            token = data["token"]
            interest_list = data['interest']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        
        try:
            email = auth.token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            interest.user_interest(email, interest_list)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response
    response.status_code = 405
    return response
