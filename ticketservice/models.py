from django.db import models

class Address(models.Model):
    postal_code = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    locality = models.CharField(max_length=30)
    number = models.CharField(max_length=4)

class User_details(models.Model):
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)

class Role(models.Model):
    role = models.CharField(max_length=30)

class User(models.Model):
    id_user_details = models.ForeignKey(User_details, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)    
    email = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    enabled = models.BooleanField()
    salt = models.IntegerField()
    created_at = models.DateField()

class Event_type(models.Model):
    name = models.CharField(max_length=30)

class Area(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    capacity = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=30)
    event_type = models.ForeignKey(Event_type, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Discount(models.Model):
    discount = models.FloatField()

class Ticket_type(models.Model):
    name = models.CharField(max_length=30)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

class Ticket(models.Model):
    number = models.CharField(max_length=30)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.FloatField()
    ticket_type = models.ForeignKey(Ticket_type, on_delete=models.CASCADE)
    
class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    
