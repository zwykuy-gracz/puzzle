from django.contrib import admin

from .models import (Hotm, FablesOfGrimforest, TheSandEmpire,
                    GuardiansOfTeltoc, EasterEvent, PiratesOfCorellia,
                    KnightsOfAvalon)

admin.site.register(Hotm)
admin.site.register(FablesOfGrimforest)
admin.site.register(TheSandEmpire)
admin.site.register(GuardiansOfTeltoc)
admin.site.register(EasterEvent)
admin.site.register(PiratesOfCorellia)
admin.site.register(KnightsOfAvalon)
