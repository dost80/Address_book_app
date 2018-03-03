from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


TYPES = (
    (1, 'home'),
    (2, 'work'),
    (3, 'other'),
)

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField(null=True)

class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    house_no = models.CharField(max_length=6)
    flat_no = models.IntegerField(null=True)
    person = models.ForeignKey(Person, related_name='person_address', on_delete=models.CASCADE)

class Phone(models.Model):
    phone_no = PhoneNumberField()
    no_type = models.IntegerField(choices=TYPES)
    person = models.ForeignKey(Person, related_name='person_phone', on_delete=models.CASCADE)

class Email(models.Model):
    email = models.EmailField(null=True)
    email_type = models.IntegerField(choices=TYPES)
    person = models.ForeignKey(Person, related_name='person_email', on_delete=models.CASCADE)

class Group(models.Model):
    models.ManyToManyField(Person)
