from django.urls import path

from . import views

urlpatterns = [
    path('vs/', views.home, name='vs'),
    path('3/', views.three, name='3'),
    path('4/', views.four, name='4'),
    path('5/', views.five, name='5'),
]
