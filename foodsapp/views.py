from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Food
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from foodsapp import urls
from cart.forms import CartAddProductForm, CartAddProductFormSideBar
from django.template import loader

def index_view(request):
    return render(request, 'foodsapp/index.html')
    
def foods(request):
    foods = Food.objects.order_by('-likes')
    cart_product_form = CartAddProductForm()
    cart_product_form2 = CartAddProductFormSideBar()
    user = request.user
    context = {
        'user' : user,
        'foods': foods,
        'cart_product_form': cart_product_form,
        'cart_product_form2': cart_product_form2
    }
    return render(request, 'foodsapp/menu.html', context)


def product_detail(request, id):
    food = get_object_or_404(Food, id=id)
    cart_product_form = CartAddProductForm()
    context = {
        'food': food,
        'cart_product_form': cart_product_form
    }
    return render(request, 'foodsapp/detail.html', context)    