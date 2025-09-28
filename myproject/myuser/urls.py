from django.urls import path
from .views import *
urlpatterns = [
    path('',Home ,name='home'),
    path('Login/',Login),
    path('Logout/',Logout),
    path('Register/',Register),   
]