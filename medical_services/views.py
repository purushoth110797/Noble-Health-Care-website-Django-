# Import render
from django.shortcuts import render


# Creating the multiple sub view for the apps
# Function for the service list view
def list(request):
    return render(request, "list.html")


# Function for the service details view
def details(request):
    return render(request, "details.html")


# Function for the service pricing and insurance info view
def pricing_info(request):
    return render(request, "pricing_info.html")
