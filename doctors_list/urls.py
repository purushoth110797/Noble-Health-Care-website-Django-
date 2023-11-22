from django.urls import path

# Importing all function from the views
from . import views

urlpatterns = [
    path("doctors/", views.doctors),
    path("doctor_profile/", views.doctor_profile),
    path("search_doctors/", views.search_doctors, name="search_doctors"),
    path("search_doctors_list/", views.search_doctors_list, name="search_doctors_list"),
    path("doctors_availability/", views.doctors_availability),
]
