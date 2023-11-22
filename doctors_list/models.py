from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    study = models.CharField(max_length=255)
    registrationNo = models.CharField(max_length=20)
    language = models.CharField(max_length=100)
    experienceYears = models.PositiveIntegerField()
    speciality = models.CharField(max_length=100)
    profile = models.TextField()

    # new field for the status:
    status = models.CharField(
        max_length=50,
        choices=[
            ("available", "Available"),
            ("notAvailable", "Not Available"),
        ],
        default="available",
    )

    def __str__(self):
        return self.name
