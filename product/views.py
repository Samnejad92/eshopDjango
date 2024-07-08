from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def products_list_view(request: HttpRequest):
    # print(HttpResponse= render(request,'products.html'))
    return render(request,'products/products.htm')

def products_detail_view(request: HttpRequest):
    return render(request,'products/details.html')