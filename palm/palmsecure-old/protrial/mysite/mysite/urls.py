# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from main.views import home_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Mapping root URL to home_view function
    path('', include('main.urls')),


   
]
