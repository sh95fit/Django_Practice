from django.urls import path, include

from rest_framework import routers

from .views import InfoViewSet
# from .views import index

router = routers.DefaultRouter()
router.register('s_list', InfoViewSet)


urlpatterns = router.urls
# urlpatterns = [
#   path('s_list/', index)
# ]