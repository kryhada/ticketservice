from django.shortcuts import render
from django.http import HttpResponse
from ticketservice.models import User 

def index(request):
	return render(request, 'index.html', {'users' : User.objects.all()}) 
