from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),  # Handles form submission and reloads predict.html
]
