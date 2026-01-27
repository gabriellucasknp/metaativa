"""
URL configuration for metaativa_projeto project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_metaativa.urls')),
]
