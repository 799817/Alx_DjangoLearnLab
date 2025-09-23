from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include  # Add include

def home(request):
    return HttpResponse("Welcome to the Advanced API Project!")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API app URLs
]
