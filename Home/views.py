from django.shortcuts import render, redirect
from .models import userDetail, Achievement


# Creating the different view for the homepage


# Homepage
def Homepage(request):
    return render(request, "index.html")


# Overview
def overview(request):
    return render(request, "overview.html")


# vision_mission
def vision_mission(request):
    return render(request, "vision_mission.html")


# Awards
def awards(request):
    data = Achievement.objects.all()
    return render(request, "awards.html", {"data": data})


# Gallery
def gallery(request):
    return render(request, "gallery.html")


# Careers
def careers(request):
    return render(request, "careers.html")


# creating view for booking form
def booking_form(request):
    return render(request, "booking_form.html")


# creating the view for the add the patient data in our database
def addBookingDetails(request):
    # Getting all the fields from the form
    firstName = request.POST["firstName"]
    middleName = request.POST["middleName"]
    lastName = request.POST["lastName"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    phoneNumber = request.POST["phoneNumber"]
    department = request.POST["department"]
    preferredDate = request.POST["preferredDate"]
    preferredTime = request.POST["preferredTime"]
    medicalConcern = request.POST["medicalConcern"]
    address = request.POST["address"]
    # create a row and adding the user data on the database:
    userDetail.objects.create(
        firstName=firstName,
        middleName=middleName,
        lastName=lastName,
        gender=gender,
        email=email,
        phoneNumber=phoneNumber,
        department=department,
        preferredDate=preferredDate,
        preferredTime=preferredTime,
        medicalConcern=medicalConcern,
        address=address,
    ).save()
    return redirect("/Home/")
