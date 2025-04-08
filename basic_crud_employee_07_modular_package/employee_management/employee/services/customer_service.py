from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

