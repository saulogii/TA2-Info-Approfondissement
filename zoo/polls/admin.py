from django.contrib import admin

# Register your models here.
from .models import Etat, Lieu, Animal

admin.site.register(Etat)
admin.site.register(Lieu)
admin.site.register(Animal)