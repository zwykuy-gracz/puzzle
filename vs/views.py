from django.shortcuts import render

from .models import ThreeStars, FourStars, FiveStars

def home(request):
    three = ThreeStars.objects
    four = FourStars.objects
    five = FiveStars.objects

    return render(request, 'vs/home.html', {'three':three, 'four':four, 'five':five})

def three(request):
    three = ThreeStars.objects
    
    return render(request, 'vs/3.html', {'three':three})

def four(request):
    four = FourStars.objects

    return render(request, 'vs/4.html', {'four':four})

def five(request):
    five = FiveStars.objects

    return render(request, 'vs/5.html', {'five':five})
