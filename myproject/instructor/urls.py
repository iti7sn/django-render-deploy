from django.urls import path
from .views import *
urlpatterns = [
    path('',allinstructor ,name='allinstructor'),
    path('instructorid/',getinstructorid),
    path('Insert/',insertinstructor,name='insertinstructor'),
    path('Update/<int:id>',updateinstructor,name='updateinstructor'),
    path('Dalete/<int:id>',deleteinstructor,name='deleteinstructor'),
    path('Inactive/<int:id>',Inactiveinstructor,name='Inactiveinstructor'),
]