
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.holamundo,name='home'),
    path('admin/', admin.site.urls),
    path('users/login',views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('users/registro', views.registro, name='register'),
    path('productos/',include('Tienda_online.urls')),
    path('carrito/', include('carts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)