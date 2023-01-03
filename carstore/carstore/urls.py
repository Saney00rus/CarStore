from django.contrib import admin
from django.urls import path, include
from store.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'cars', CarstoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
