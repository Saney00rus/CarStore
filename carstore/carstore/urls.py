from django.contrib import admin
from django.urls import path, include
from store.views import *
from .yasg import urlpatterns as swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/cars/', CarstoreAPIList.as_view()),
    path('api/cars/<int:pk>/', CarstoreAPIUpdate.as_view()),
    path('api/carsdelete/<int:pk>/', CarstoreAPIDestroy.as_view()),
]

urlpatterns += swagger