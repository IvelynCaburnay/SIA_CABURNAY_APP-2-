from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm


def Home(request):

    pets = Pet.objects.all()

    form = PetForm()

    context = {
        'pets': pets,
        'form': form
    }

    return render(request, 'dashboard.html', context)


def AddPet(request):

    if request.method == 'POST':

        form = PetForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = PetForm()

    context = {
        'form': form
    }

    return render(request, 'add_pet.html', context)