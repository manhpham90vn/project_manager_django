from django.http import HttpResponse
from django.shortcuts import render
from .models import Client

# Create your views here.
def index(request):
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients})

def update(request, id):
    return HttpResponse("You're updating client %s." % id)

def delete(request, id):
    return HttpResponse("You're deleting client %s." % id)