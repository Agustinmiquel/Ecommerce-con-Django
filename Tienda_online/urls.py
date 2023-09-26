from django.urls import path

from . import views

urlpatterns = [
    path('<pk>', views.ProductDetailsView.as_view(), name='product')
]