from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


from apps.mascota.forms import MascotaForm


def index(request):
    return render(request,'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST': 
        form = MascotaForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('mascota:index')
        else:
            form = MascotaForm() 
        return render(request, 'mascota/mascota_form.html', {'form':form})
       


