# ecommerce/urls.py

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),# Include the core app's URLs
    path('auth/', include('userauths.urls')) 
    
]
