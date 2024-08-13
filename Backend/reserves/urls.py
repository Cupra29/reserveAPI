from rest_framework import routers
from .api import ReserveViewSet

router = routers.DefaultRouter()

# Rutas de la API
router.register('api/reserves', ReserveViewSet, 'reserves')

urlpatterns = router.urls