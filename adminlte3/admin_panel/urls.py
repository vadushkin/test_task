from django.urls import path, include
from rest_framework import routers

from . import views
from .api import NewsViewSet

router = routers.SimpleRouter()

router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('add-product/', views.add_products, name='add-product'),
    path('api/v1/', include(router.urls)),
]
