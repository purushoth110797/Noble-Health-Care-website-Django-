# Import render
from django.shortcuts import render, get_object_or_404, redirect

# import models in the view
from Home.models import userDetail


# Creating the multiple views for the appointment page
# Function for the Booking form:
def booking_form(request):
    return render(request, "booking_form1.html")


# Function for the booking status:
def booking_status(request):
    userData = userDetail.objects.all()
    return render(request, "booking_status.html", {"userData": userData})


# Function for the view the edit booking page:
def edit(request):
    # filtering the database to get only waiting and confirmed data
    waitingAndConfirmedData = userDetail.objects.filter(
        status__in=["waiting", "confirmed"]
    )
    # rendering the html file
    return render(
        request, "edit.html", {"waitingAndConfirmedData": waitingAndConfirmedData}
    )


# Function for the cancel page:
def cancel(request):
    # filtering the database to get only waiting and confirmed data
    waitingAndConfirmedData = userDetail.objects.filter(
        status__in=["waiting", "confirmed"]
    )
    # rendering the html file
    return render(
        request, "cancel.html", {"waitingAndConfirmedData": waitingAndConfirmedData}
    )


# Function for the booking history page:
def history(request):
    # filtering the database to get only waiting and confirmed data
    completedData = userDetail.objects.filter(status__in=["completed"])
    # rendering the html file
    return render(request, "history.html", {"completedData": completedData})


# view to edit the user data:
def editUser(request, id):
    # Retrieve the data
    userData = get_object_or_404(userDetail, id=id)
    return render(request, "edit_form.html", {"userData": userData})


# function or view to update the database with new data
def userDetailUpdate(request, id):
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
    userDetail.objects.filter(id=id).update(
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
    )
    return redirect("/appointment/booking_status/")


# function or view to cancel the booking
def cancelBooking(request, id):
    userDetail.objects.filter(id=id).delete()
    return redirect("/appointment/cancel/")
