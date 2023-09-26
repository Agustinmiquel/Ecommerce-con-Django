from django.shortcuts import render

from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product.html'
