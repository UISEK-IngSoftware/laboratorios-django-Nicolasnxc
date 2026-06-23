"""
URL configuration for pokedex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from lab8 import settings
from django.contrib.auth.views import LogoutView # <-- IMPORTANTE IMPORTAR ESTO

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    
    # Ruta para la autenticación con Django OAuth Toolkit
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), 
    
    # Rutas de tu aplicación Pokedex
    path('', include('pokedex.urls'))
=======
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('pokedex.urls')),
    path('api/', include('api.urls')), 
>>>>>>> a5c6ce8190ac06cb3294de6115736b90d3855c9d
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)