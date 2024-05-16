"""
URL configuration for fleet project.
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from taxi.urls import router

urlpatterns = [
    path('', include(router.urls))
]
