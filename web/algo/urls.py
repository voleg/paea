from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'algos', DatabaseViewSet)
