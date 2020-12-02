from django.db import models
from django.utils import timezone


class Imychestvo(models.Model):
    Name = models.CharField(null=True, max_length=200, help_text="Введите название имущества")
    Description = models.TextField()
    Type_of_property = models.CharField(max_length=100)
    def _str_(self):
        return self.Name

class Contract(models.Model):
    Name_contract = models.CharField(null=True, max_length=200, help_text="Введите название договора")
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    imychestvo = models.ForeignKey('Imychestvo', on_delete=models.SET_NULL, null=True)
    Sum = models.IntegerField()
    Revenue_contract = models.IntegerField()
    text = models.TextField()
    def _str_(self):
         return self.Name_contract

class Client(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Fathername = models.CharField(max_length=50)
    Date_of_birth = models.DateTimeField(default=timezone.now)
    Passport_series = models.IntegerField(null=True)
    Passport_number = models.IntegerField(null=True)
    Address = models.CharField(max_length=300)
    Phone_number = models.IntegerField()

    def _str_(self):
        return self.Name

