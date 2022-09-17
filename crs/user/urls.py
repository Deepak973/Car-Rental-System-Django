from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('reg', views.register),
    path('log',views.login),
    path('home/',views.home),
    path('logout',views.logout),
    path('bar/',views.bookaridel),
    path('barv',views.bookaridev),
    path('bookv/<int:id>/<str:sdate>/<str:edate>',views.bookvehicle),
    path('booked/',views.booked),
    path('completed/',views.completed),
    path('cancelled/',views.cancelled),
    path('cancelbooking/<str:bookingid>',views.cancelbooking),
    path('cancelbookingconfirm/<str:bookingid>/<str:refund_amt>',views.cancelbookingconfirm),
    path('contactus/',views.contactus),
    path('payment/',views.payment),
    path("additional/<str:booking_id>",views.additionalcharges),
    
    
   
]