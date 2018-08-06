from django.shortcuts import render
from django.db.models import Count

from .models import Camp1, Camp2



def camp1(request):
    c1 = Camp1.objects
    three = Camp1.objects.filter(stars__exact=3).count()
    four = Camp1.objects.filter(stars__exact=4).count()
    five = Camp1.objects.filter(stars__exact=5).count()
    cz = Camp1.objects.count()+ Camp2.objects.count()
    threeSum = Camp2.objects.filter(stars__exact=3).count() + three
    fourSum = Camp2.objects.filter(stars__exact=4).count() + four
    fiveSum = Camp2.objects.filter(stars__exact=5).count() + five
    threeStat = round((threeSum/cz)*100)
    fourStat = round((fourSum/cz)*100)
    fiveStat = round((fiveSum/cz)*100)
    return render(request, 'camps/1.html', {'c1':c1, 'three':three, 'four':four,
                                            'five':five, 'cz':cz, 'threeSum':threeSum,
                                            'fourSum':fourSum, 'fiveSum':fiveSum,
                                            'threeStat':threeStat, 'fourStat':fourStat,
                                            'fiveStat':fiveStat})

def camp2(request):
    c2 = Camp2.objects
    three = Camp2.objects.filter(stars__exact=3).count()
    four = Camp2.objects.filter(stars__exact=4).count()
    five = Camp2.objects.filter(stars__exact=5).count()
    cz = Camp1.objects.count()+ Camp2.objects.count()
    threeSum = Camp1.objects.filter(stars__exact=3).count() + three
    fourSum = Camp1.objects.filter(stars__exact=4).count() + four
    fiveSum = Camp1.objects.filter(stars__exact=5).count() + five
    threeStat = round((threeSum/cz)*100)
    fourStat = round((fourSum/cz)*100)
    fiveStat = round((fiveSum/cz)*100)
    return render(request, 'camps/2.html', {'c2':c2, 'three':three, 'four':four,
                                            'five':five, 'cz':cz, 'threeSum':threeSum,
                                            'fourSum':fourSum, 'fiveSum':fiveSum,
                                            'threeStat':threeStat, 'fourStat':fourStat,
                                            'fiveStat':fiveStat})
