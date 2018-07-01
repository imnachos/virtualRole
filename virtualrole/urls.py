from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('main.urls')),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
