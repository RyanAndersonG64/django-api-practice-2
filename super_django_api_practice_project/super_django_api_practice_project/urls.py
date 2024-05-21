"""
URL configuration for super_django_api_practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers

from super_django_practice_app.views import *

router = routers.DefaultRouter()

router.register(r'vehicles', VehicleViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'customerOrders', CustomerOrderViewSet)


urlpatterns = [
    path('', include(router.urls))
]