from django.urls import path

from . import views

urlpatterns = [
    #main website
    path("fr/", views.accueilfr, name="accueilfr"),
    path("contact/fr", views.contactfr, name="contactfr"),
    path("resume/fr", views.resumefr, name="resumefr"),
    path("project/fr", views.projectfr, name="projectfr"),

    path("", views.accueileng, name="accueileng"),
    path("contact/", views.contacteng, name="contacteng"),
    path("resume/", views.resumeeng, name="resumeeng"),
    path("project/", views.projecteng, name="projecteng"),

    
]