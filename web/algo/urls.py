from rest_framework.routers import DefaultRouter

from algo.views import CalculationViewSet


router = DefaultRouter()
router.register(r'algo', CalculationViewSet, basename='calculations')

urlpatterns = router.urls
