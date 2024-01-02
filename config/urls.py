from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.users.router import router as users_api
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


api_router = DefaultRouter()
api_router.registry.extend(users_api.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
    
    # SWAGGER
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
    
    # UNCOMMENT IF YOU USE BROWSABLE API
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# DJANGO-DEBUG-TOOLBAR
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
