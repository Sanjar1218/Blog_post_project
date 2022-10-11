from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('databaseApp.urls')),
    path('admin/', admin.site.urls),
]
