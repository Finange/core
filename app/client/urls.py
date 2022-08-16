from rest_framework.routers import DefaultRouter

from .api import ClientViewSet

router = DefaultRouter()

router.register("client", ClientViewSet, basename="user")

urlpatterns = router.urls
