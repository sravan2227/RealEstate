from django.contrib import admin
from django.urls import path, include

# we need to add all the apps url patterns here
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
