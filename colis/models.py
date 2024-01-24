from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_administrateur = models.BooleanField('administrateur', default=False)
    is_client = models.BooleanField('client', default=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
   
class Coli(models.Model):
    typeColi = models.CharField(max_length=50)
    lieuDepart = models.CharField(max_length=50)
    lieuArriver = models.CharField(max_length=50)
    villeArriver = models.CharField(max_length=50,default='pas de ville')
    expedi = models.CharField(max_length=50)
    desti = models.CharField(max_length=50)
    kilo = models.IntegerField(default=0,null=True)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    created_coli = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=100,default="Pas de details")
    codeColi = models.CharField(max_length=50)
    image = models.FileField(upload_to='images',blank=True,default='aucune image')
    class Meta:
        verbose_name = 'Coli'
        verbose_name_plural = 'Colis'
    def __str__(self):
        return self.typeColi

class Contact(models.Model):
    noms = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    sujet = models.CharField(max_length=50,default='pas de sujet')
    message = models.TextField(max_length=100,default="Pas de message")
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
   
    
