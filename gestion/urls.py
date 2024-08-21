from django.urls import path

from . import views

urlpatterns = [
    #main website
    path("", views.admin, name="admin"),
    path("login/", views.login_view, name="login"),
    path('logout/',views.logout_view ,name='logout'),

]