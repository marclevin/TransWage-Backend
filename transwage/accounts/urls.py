from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from .views import JobViewSet, ContractViewSet


router = routers.DefaultRouter()
router.register(r"jobs", JobViewSet)
router.register(r"contracts", ContractViewSet)

urlpatterns = [path("", include(router.urls)), path("login", obtain_auth_token)]
