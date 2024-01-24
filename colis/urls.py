from django.urls import path, include
from .views import *

urlpatterns = [
   path('',home, name='home'),
   path('connexion', connexion, name='connexion'),
   path('tarif', tarif, name='tarif'), 
   path('service', service, name='service'),
   path('contact', contact, name='contact'),
   path('enreg_colis', enreg_colis, name='enreg_colis'),
   path('list_colis', list_colis, name='list_colis'),
   path('contact', contact, name='contact'),
   path('list_message', list_message, name='list_message'),
   path('update_coli/id=<int:id>', update_coli, name='update_coli'),
   path('delete_coli/id=<int:id>', delete_coli, name='delete_coli'),
   path('deconnexion',deconnexion, name='deconnexion'),  
]