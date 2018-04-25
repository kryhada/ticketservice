from django.db import models

class User(models.Model):
    id_user_details = models.ForeignKey(User_details, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)    
    email = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    enabled = models.BooleanField()
    salt = models.IntegerField()
    created_at = models.DateField()

class User_details(models.Model):
    id_address = models.ForeignKey(Address, on on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)

class Role(models.Model):
    role = models.CharField(max_length=30)

class Address(models.Model):
    postal_code = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    locality = models.CharField(max_length=30)
    number = models.CharField(max_length=4)

