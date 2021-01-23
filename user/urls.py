from . import views
from django.urls import path
urlpatterns=[
    path('',views.login, name='user_login'),
    path('signup/',views.signup, name='sighnup'),
    path('logout/',views.logout, name='logout'),
    path('userhome/',views.userhome, name='userhome'),
   
]