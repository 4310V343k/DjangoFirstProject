from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', include('mangalib.api.urls')),
]
