from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render


from django.db.models import Q

from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product.html'

class ProductSearchViewList(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query()) 
        return Product.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        print(context)
        return context