from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BRCA1BreastViewSet, BRCA1OvarineViewSet, BRCA2BreastViewSet, BRCA2OvarineViewSet, PALB2BreastViewSet, PALB2OvarineViewSet



router = DefaultRouter()


router.register('BRCA1Breast', BRCA1BreastViewSet)
router.register('BRCA1Ovarin', BRCA1OvarineViewSet)
router.register('BRCA2Breast', BRCA2BreastViewSet)
router.register('BRCA2Ovarin', BRCA2OvarineViewSet)
router.register('PALB2Breast', PALB2BreastViewSet)
router.register('PALB2Ovarin', PALB2OvarineViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
