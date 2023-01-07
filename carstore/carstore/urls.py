from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from store.views import *
from .yasg import urlpatterns as swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/cars/', CarstoreAPIList.as_view()),
    path('api/cars/<int:pk>/', CarstoreAPIUpdateAndDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += swagger

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)