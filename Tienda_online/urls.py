from django.urls import path

from . import views

urlpatterns = [
    path('search', views.ProductSearchViewList.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailsView.as_view(), name='product'),
]