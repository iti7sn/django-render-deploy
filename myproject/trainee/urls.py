from django.urls import path
from .views import *
urlpatterns = [
    path('',alltrainee ,name='alltrainee'),
    path('traineeid/',gettraineeid),
    path('Insert/',inserttrainee,name='inserttrainee'),
    path('Update/<int:id>',updatetrainee,name='updatetrainee'),
    path('Dalete/<int:id>',deletetrainee,name='deletetrainee'),
    path('Inactive/<int:id>',Inactive,name='Inactive'),
]