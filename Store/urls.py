
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('',views.holamundo,name='home'),
    path('admin/', admin.site.urls),
    path('users/login',views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('users/registro', views.registro, name='register'),
    path('productos/',include('Tienda_online.urls'))
]
