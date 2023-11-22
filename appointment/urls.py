from django.urls import path, include

# Importing all the function from views
from . import views

# URLs for the appointment page view
urlpatterns = [
    path("Home/", include("Home.urls")),
    path("booking_form/", views.booking_form),
    path("booking_status/", views.booking_status),
    path("edit/", views.edit),
    path("cancel/", views.cancel),
    path("history/", views.history),
    path("editUser/<int:id>/", views.editUser, name="edit_booking"),
    path("userDetailUpdate/<int:id>/", views.userDetailUpdate, name="update_booking"),
    path("cancelBooking/<int:id>/", views.cancelBooking, name="cancel_booking"),
]
