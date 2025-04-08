from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nid = models.IntegerField()
    email = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.firstName} {self.lastName}"

