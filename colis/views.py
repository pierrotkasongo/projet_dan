from projet_dan import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')
def tarif(request):
    return render(request,'tarif.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    if request.method == 'POST':
        noms = request.POST['noms'].lower()
        mail = request.POST['mail'].lower()
        sujet = request.POST['sujet'].lower()
        message = request.POST['message'].lower()
        new_contact= Contact.objects.create(noms=noms, mail=mail,sujet=sujet, message=message)
        new_contact.save()
    return render(request,'contact.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password'].lower()
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_administrateur:
            login(request, user)
            return redirect('enreg_colis')

        elif user is not None and user.is_client:
            login(request, user)
            return redirect('client')
        else:
            messages.error(request, "Erreur sur l'dentification")
            return render(request, 'login.html')
    return render(request,'login.html')



@login_required
def enreg_colis(request):
    prix=5
    total=0
    if request.user.is_authenticated:
        page = 'colis'
        administrateurs = User.objects.filter(is_administrateur=True).order_by('username')
        
        if request.method == 'POST':
            typeColi = request.POST['typeColi'].lower()
            lieuDepart = request.POST['lieuDepart'].lower()
            lieuArriver = request.POST['lieuArriver'].lower()
            villeArriver= request.POST['villeArriver'].lower()
            expedi = request.POST['expediteur'].lower()
            desti = request.POST['destinateur'].lower()
            telephone = request.POST['telephone']
            email = request.POST['email']
            created_coli=request.POST['created_coli']
            description= request.POST['description'].lower()
            codeColi = request.POST['codeColi'].lower()
            image= request.FILES['image']
            is_administrateur=True 
            kilo=int(request.POST['kilo'])
            total=kilo*prix
            if Coli.objects.filter(codeColi=codeColi):
                messages.error(request, "Le code à été déjà utiliser !")
            else:
                new_coli= Coli.objects.create(typeColi=typeColi, lieuDepart=lieuDepart, lieuArriver=lieuArriver, villeArriver=villeArriver, expedi=expedi,desti=desti,kilo=total, telephone=telephone, email=email, created_coli=created_coli,description=description,codeColi =codeColi, image=image)
                
                if new_coli is not None:
                    messages.success(request, "Colis envoyer avec succès !")
                    sujet = "Colis envoyer est du type : " + new_coli.typeColi + " Pays de depart : " + new_coli.lieuDepart + " Pays d'arriver : "+ new_coli.lieuArriver + " La ville d'arriver :" + new_coli.villeArriver + " Nom expediteur : "+ new_coli.expedi +" Nom du destinateur : " + new_coli.desti + " Adresse email expediteur : " + new_coli.email 
                    message = "Votre mot de passe pour retirer votre colis est : " + codeColi
                    expediteur = settings.EMAIL_HOST_USER
                    destinateur = [email]
                    send_mail(sujet, message, expediteur,destinateur, fail_silently=True)
                else:
                    messages.error(request, "échoué d'envoie !")
    return render(request,'enreg_colis.html')

@login_required
def list_colis(request):
    coli= Coli.objects.all()
    if request.method == "GET":
        codeColi = request.GET.get('recherche')
        if codeColi is not None:
            coli= Coli.objects.filter(codeColi=codeColi)
    context = {
        'colis':coli,

    }
    return render(request,'listeColi.html',context)

def update_coli(request, id):
    if request.user.is_authenticated:
        colis = get_object_or_404(Coli, id=id)
        page = 'list_colis'
        if request.method == 'POST':
            typeColi = request.POST['typeColi'].lower()
            lieuDepart = request.POST['lieuDepart'].lower()
            lieuArriver = request.POST['lieuArriver'].lower()
            villeArriver= request.POST['villeArriver'].lower()
            expediteur = request.POST['expediteur'].lower()
            destinateur = request.POST['destinateur'].lower()
            kilo=int(request.POST['kilo'])
            telephone = request.POST['telephone']
            email = request.POST['email']
            created_coli=request.POST['created_coli']
            description= request.POST['description'].lower()
            codeColi = request.POST['codeColi'].lower()
            image= request.FILES['image']
            objet = Coli.objects.get(id=id)
            objet.typeColi = typeColi
            objet.lieuDepart = lieuDepart
            objet.lieuArriver = lieuArriver
            objet.villeArriver = villeArriver
            objet.expediteur = expediteur
            objet.destinateur = destinateur
            objet.telephone = telephone
            objet.email = email
            objet.created_coli = created_coli
            objet.description = description
            objet.codeColi = codeColi
            objet.image = image
            objet.save()
            return redirect('list_colis')
        return render(request, 'update_coli.html',{'colis':colis,'coli':page})
    else:
        return redirect('connexion')


@login_required
def delete_coli(request, id):
    if request.user.is_authenticated:
        coli = get_object_or_404(Coli, id=id)
        coli.delete()
        return redirect('list_colis')
    else:
        return redirect('connexion')
    
@login_required
def list_message(request):
    contact= Contact.objects.all()
    context = {
        'contacts':contact,
    }
    return render(request,'listeMessage.html',context)

@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')