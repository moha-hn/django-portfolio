
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('adminn/', admin.site.urls),
    path('',include("myapp.urls")),
    path("gestion/", include("gestion.urls")),
]
