from django.urls import path

# Importing everything from views
from . import views


# inserting the URL of the views
urlpatterns = [
    path("", views.Homepage),
    path("overview/", views.overview),
    path("vision_mission/", views.vision_mission),
    path("awards/", views.awards),
    path("gallery/", views.gallery),
    path("careers/", views.careers),
    path("booking_form/", views.booking_form),
    path("booking_form/addBookingDetails", views.addBookingDetails),
]
