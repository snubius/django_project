from django.shortcuts import render
from . import models
from.models import product

def list_products(request):
    users = product.objects.all()
    print(locals())
    return render(request, 'page.html', locals())

