from django.db import models


# model for the booking
class userDetail(models.Model):
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200, blank=True, null=True)
    lastName = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    email = models.EmailField(max_length=200)
    phoneNumber = models.IntegerField()
    department = models.CharField(max_length=50)
    preferredDate = models.DateField()
    preferredTime = models.CharField(max_length=50)
    medicalConcern = models.TextField()
    address = models.TextField(max_length=300)

    # new field for the status:
    status = models.CharField(
        max_length=50,
        choices=[
            ("confirmed", "Confirmed"),
            ("waiting", "Waiting"),
            ("completed", "Completed"),
        ],
        default="waiting",
    )

    # Function for getting the full name
    def full_name(self):
        # Concatenate first, middle, and last names
        parts = [self.firstName, self.middleName, self.lastName]
        # Filter out empty parts (e.g., if middle_name is blank)
        name_parts = [part for part in parts if part]
        return " ".join(name_parts)

    def __str__(self):
        return self.firstName


# models for achievement sections
class Achievement(models.Model):
    # function to create the field
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
