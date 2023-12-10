from django.urls import path
from .views import signup_method

urlpatterns = [
    path('signup/', signup_method, name='signup_method'),
]