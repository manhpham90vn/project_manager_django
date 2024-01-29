from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm

# Create your views here.
def index(request):
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients})

def show(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, 'show.html', {'client': client})

def new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()    
    return render(request, 'new.html', {'form': form})

def update(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm(instance=client)    
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('index')