from django.urls import path

from . import views


urlpatterns = [
    path('hotm/', views.hotm, name='hotm'),
    path('fables-of-grimforest/', views.fablesOfGrimforest, name='fables-of-grimforest'),
    path('guardians-of-teltoc/', views.guardiansOfTeltoc, name='guardians-of-teltoc'),
    path('knights-of-avalon/', views.knightsOfAvalon, name='knights-of-avalon'),
    path('pirates-of-corellia/', views.piratesOfCorellia, name='pirates-of-corellia'),
    path('easter-event/', views.easterEvent, name='easter-event'),
    path('the-sand-empire/', views.theSandEmpire, name='the-sand-empire'),
]
