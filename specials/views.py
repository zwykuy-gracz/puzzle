from django.shortcuts import render

from .models import (Hotm, FablesOfGrimforest, TheSandEmpire,
                    GuardiansOfTeltoc, EasterEvent,
                    PiratesOfCorellia, KnightsOfAvalon)

def hotm(request):
    hotm = Hotm.objects
    return render(request, 'specials/hotm.html', {'hotm':hotm})

def fablesOfGrimforest(request):
    fables = FablesOfGrimforest.objects
    return render(request, 'specials/fables-of-grimforest.html', {'fables':fables})

def theSandEmpire(request):
    sand = TheSandEmpire.objects
    return render(request, 'specials/the-sand-empire.html', {'sand':sand})

def guardiansOfTeltoc(request):
    guardians = GuardiansOfTeltoc.objects
    return render(request, 'specials/guardians-of-teltoc.html', {'guardians':guardians})

def easterEvent(request):
    easter = EasterEvent.objects
    return render(request, 'specials/easter-event.html', {'easter':easter})

def piratesOfCorellia(request):
    pirates = PiratesOfCorellia.objects
    return render(request, 'specials/pirates-of-corellia.html', {'pirates':pirates})

def knightsOfAvalon(request):
    knights = KnightsOfAvalon.objects
    return render(request, 'specials/knights-of-avalon.html', {'knights':knights})
