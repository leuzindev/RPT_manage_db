
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home_list, name='home_list'),
    path('home/<int:product_id>', views.home_id, name='home_id'),
     path('logout', views.logout, name='logout'),
    #  path('buscar', views.buscar, name='buscar'),
]
