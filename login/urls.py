from django.urls import path
from .views import login_method

urlpatterns = [
    path('login/', login_method, name='login_method'),
]