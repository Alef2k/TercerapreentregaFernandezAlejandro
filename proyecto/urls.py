"""
URL configuration for proyecto project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='aplicacion/', permanent=True)),  # Redirección a la URL de la aplicación
    #
    path('aplicacion/', include('aplicacion.urls')),
]
