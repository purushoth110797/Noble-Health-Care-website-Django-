# Import render to display the HTML file
from django.shortcuts import render
from .models import Doctor


# Creating the multiple views for the Doctor list page
# Doctor list views
def doctors(request):
    specialties = Doctor.objects.values_list("speciality", flat=True).distinct()
    doctors_by_speciality = {}

    for speciality in specialties:
        doctors_by_speciality[speciality] = Doctor.objects.filter(speciality=speciality)

    context = {"doctors_by_speciality": doctors_by_speciality}
    return render(request, "doctors.html", context)


# Doctors profile page:
def doctor_profile(request):
    specialties = Doctor.objects.values_list("speciality", flat=True).distinct()
    doctors_by_speciality = {}

    for speciality in specialties:
        doctors_by_speciality[speciality] = Doctor.objects.filter(speciality=speciality)

    context = {"doctors_by_speciality": doctors_by_speciality}
    return render(request, "doctor_profile.html", context)


# search doctors page:
def search_doctors(request):
    return render(
        request,
        "search_doctors.html",
    )


# search doctors page:
def search_doctors_list(request):
    searched_name = None
    doctors = []

    if "doctor_name" in request.GET:
        searched_name = request.GET["doctor_name"]
        doctors = Doctor.objects.filter(name__icontains=searched_name)

    return render(
        request,
        "search_doctors.html",
        {"doctors": doctors, "searched_name": searched_name},
    )


# page to check the doctor Availability:
def doctors_availability(request):
    doctors_list = Doctor.objects.all()
    return render(request, "doctors_availability.html", {"doctors_list": doctors_list})
