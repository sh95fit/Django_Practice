from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from restapi_test.views import addresses_list, addresses

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', addresses_list),
    path('addresses/<int:pk>', addresses),
]
