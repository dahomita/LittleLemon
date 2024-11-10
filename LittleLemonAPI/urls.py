"""
URL configuration for LittleLemonAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Littlelemon_app import views
from djoser import views as djoser_views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = routers.DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/', include(router.urls)), 
    path('auth/login/', djoser_views.TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/me/', djoser_views.UserDetailViewSet.as_view(), name='me')
    # ... other Djoser endpoints as needed (registration, password reset)

    # ... other URL patterns for static files, media files, etc. (if applicable)
]

# Optional error handling (customize as needed)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.conf import settings

def custom_error_handler(exc, context):
    # Handle specific exceptions (e.g., ValidationError)
    if isinstance(exc, ValidationError):
        return Response(exc.detail, status=400)

    # Fallback for other exceptions
    return Response(status=500)

if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]

# Set custom error handler (optional)
handler400 = custom_error_handler
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Littlelemon_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include, re_path
from django.views.generic import RedirectView

router = routers.DefaultRouter()
router.register(r'menu-items', 
 views.MenuItemViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', 
 include(router.urls)),

    # Djoser URLs for user registration and management (adjust as needed)
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    # Custom endpoints for token obtain and refresh (optional)
    path('auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('', RedirectView.as_view(url='/api/', permanent=False)), 

]