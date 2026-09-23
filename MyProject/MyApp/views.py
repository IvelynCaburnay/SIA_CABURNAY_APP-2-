from django.shortcuts import render
from .models import Pets

# Create your views here.
def pet(request):
    pets = Pets.objects.all()

    context ={
        'pets': pets
    }

    return render(request,'invApp/pets.html',context)
