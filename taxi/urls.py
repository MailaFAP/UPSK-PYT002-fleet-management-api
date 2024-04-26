"""urls da api"""

from rest_framework.routers import SimpleRouter
from .views import TaxiViewSet

router = SimpleRouter()
router.register('taxi' , TaxiViewSet)

