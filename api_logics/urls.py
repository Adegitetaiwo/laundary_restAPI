from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pick-up/', views.pickUp, name='pickup'),
    path('contact/', views.contact, name='contact'),
    path('testimonial/', views.testimonials, name='testimonial'),
    path('testimonial/<int:pk>/', views.testimonial, name='testimonial')


]
