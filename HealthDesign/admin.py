from django.contrib import admin
from .models import Demographics, Guardian, Allergies

admin.site.register(Demographics)
admin.site.register(Guardian)
admin.site.register(Allergies)
