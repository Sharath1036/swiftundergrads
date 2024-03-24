from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name= 'home'),
    path("about", views.about, name= 'about'),
    path("mumbai-counselling", views.mumbai, name= 'mumbai'),
    path("maharashtra-counselling", views.maharashtra, name= 'maharashtra'),
    path('payment/<str:original_amount>/<str:discount>/<str:final_amount>/<path:image>/', views.payment, name='payment'),
    path('success', views.success, name='success'),
    path("mhtcet-notes", views.cetnotes, name= 'cetnotes'),
    path("engineering-notes", views.enggnotes, name= 'enggnotes'),
    path("pharmacy-notes", views.pharmnotes, name= 'pharmnotes'),
    path("contact", views.contact, name= 'contact'),
]

