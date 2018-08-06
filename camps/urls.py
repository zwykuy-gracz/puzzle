from django.urls import path

from . import views

urlpatterns = [
    path('1/', views.camp1, name='1'),
    path('2/', views.camp2, name='2'),
]
