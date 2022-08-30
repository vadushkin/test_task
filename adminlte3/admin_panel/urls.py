from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-product/', views.add_products, name='add-product'),
]
