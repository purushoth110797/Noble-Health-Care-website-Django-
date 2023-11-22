# import the path function
from django.urls import path

# Import all the function from the views
from . import views

# URLs for the imported views
urlpatterns = [
    path("list/", views.list),
    path("details/", views.details),
    path("pricing_info/", views.pricing_info),
]
