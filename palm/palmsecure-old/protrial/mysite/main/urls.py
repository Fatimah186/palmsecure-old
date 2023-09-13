# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('capture_frames/', views.capture_frames_view, name='capture_frames'),
]
