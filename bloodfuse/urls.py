from django.contrib import admin
from django.urls import path, include
from bloodfuse.view import redirect_to_index
from rest_framework import permissions

# drf-yasg imports
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# rest_framework_simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from .view import update_from_github

schema_view = get_schema_view(
    openapi.Info(
        title="BloodFuse API Endpoint",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Site
    path('', redirect_to_index, name="redirect_to_index"),
    path('api/', include('core.urls')),
    path('_/', admin.site.urls),
    # path("update_from_github", update_from_github, name="update_from_github"),

    # dj-auth endpoints
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),

    # Swagger Api endpoints
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # rest_framework_simplejwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

'''
This above re_path exposes 4 endpoints:

    A JSON view of your API specification at /api/swagger.json
    A YAML view of your API specification at /api/swagger.yaml
    A swagger-ui view of your API specification at /api/swagger/
    A ReDoc view of your API specification at /api/redoc/

'''