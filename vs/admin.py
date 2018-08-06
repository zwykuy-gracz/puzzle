from django.contrib import admin

from .models import ThreeStars, FourStars, FiveStars

admin.site.register(ThreeStars)
admin.site.register(FourStars)
admin.site.register(FiveStars)
