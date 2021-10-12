from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.http.response import JsonResponse
from product.errors import ProductIdError
import product.products as products
import json

# Create your views here.

def view_product_user(request):
 
    response = HttpResponse()
    if request.method == "GET":
        # try:
        #     data = json.loads(request.body)
        # except json.JSONDecodeError:
        #     response.status_code = 441
        #     response.content = 'json.JSONDecodeErro'
        #     return response
        
        try:
            product_id = request.GET.get("product_id")
        except KeyError:
            response.status_code = 442
            response.content = "format is wrong"
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
