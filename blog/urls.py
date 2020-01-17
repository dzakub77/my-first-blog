
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #nazwa URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
# 'post/<int:pk>/' - ogólnie jest to wzorzec URL: post/ - oznacza że adres URL powinien
# zaczynać się od słowa post, po którym nastąpi /. <int:pk> - oznacza że Django
# spodziewa się liczby całkowitej i przekaże jej wartość do widoku jako zmienną pk
# i znów potrzebujemy / zanim zakonczymy wzorzec URL