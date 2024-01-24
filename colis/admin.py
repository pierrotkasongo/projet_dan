from django.contrib import admin
from .models import *

# Register your models here.

class AdminColi(admin.ModelAdmin):
    list_display = ("typeColi", "lieuDepart", "lieuArriver","villeArriver","expedi","desti","kilo","telephone","email","created_coli","description","codeColi","image")
admin.site.register(Coli, AdminColi)
admin.site.register(User)

class AdminContact(admin.ModelAdmin):
    list_display = ("noms", "mail","sujet","message")
admin.site.register(Contact, AdminContact)

