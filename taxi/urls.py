"""urls da api"""

from rest_framework.routers import SimpleRouter
from .views import TaxiViewSet , TaxiLocationView

router = SimpleRouter()
router.register('taxi' , TaxiViewSet)
router.register('taxi_locations', TaxiLocationView)
