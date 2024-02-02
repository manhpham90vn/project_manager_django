from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

# Create your views here.
def index(request):
    clients = Client.objects.all().order_by('id')
    return render(request, 'client/index.html', {'clients': clients})

def show(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, 'client/show.html', {'client': client})

def new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()    
    return render(request, 'client/new.html', {'form': form})

def update(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm(instance=client)    
    return render(request, 'client/update.html', {'form': form})

def delete(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('index')