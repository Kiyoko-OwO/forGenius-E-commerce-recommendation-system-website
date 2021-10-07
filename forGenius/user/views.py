from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import user.auth as auth

# Create your views here.
@csrf_exempt
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
        auth.auth_register(email, name, password)
        response.status_code = 200
        return response
    response.status_code = 400
    return response
