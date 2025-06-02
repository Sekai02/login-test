from django.contrib import admin
from django.urls import path,include
from auth_module.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('auth_module.urls')),
    path('',home, name='home'),
]
