from django.urls import path
from loginapp import views

urlpatterns=[
    path('register/',views.login,name='register'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('logout/',views.logout,name='logout'),


    ]