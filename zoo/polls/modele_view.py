from .models import *

def lit_état(animal):
    if animal in Animal.objects.all():
        return animal.etat.etat_text
    else:
        return None

def lit_lieu(animal):
    if animal in Animal.objects.all():
        return animal.lieu.equipement_text
    else:
        return None

def vérifie_disponibilité(équipement_name):
    équipement = Lieu.objects.get(equipement_text=équipement_name)
    if équipement in Lieu.objects.all(): 
        return équipement.disponibilite
    else:
        return None

def cherche_occupant(lieu_name):
    lieu = Lieu.objects.get(equipement_text=lieu_name)
    if lieu in Lieu.objects.all():
        liste = []
        for animal in Animal.objects.all():
            if animal.lieu == lieu :
                liste.append(animal.animal_name)
        liste = ','.join(map(str, liste))
        return liste
    else:
        return None

def change_état(animal, etat_name):
    etat = Etat.objects.get(etat_text = etat_name)
    if animal in Animal.objects.all():
        if etat in Etat.objects.all():
            animal.etat = etat
        animal.save()

def change_lieu(animal, lieu_name):
    lieu = Lieu.objects.get(equipement_text=lieu_name)
    if animal in Animal.objects.all():
        if lieu in Lieu.objects.all():
            if lieu.disponibilite!='occupé':
                lieu_vacant = animal.lieu
                animal.lieu = lieu
                if lieu.equipement_text != 'litière':
                    lieu.disponibilite='occupé'
                lieu_vacant.disponibilite='libre'
                lieu_vacant.save()
            lieu.save()
        animal.save()
    
    

