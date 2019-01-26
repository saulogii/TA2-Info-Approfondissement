from .modele_view import *

def nourrir(animal):
    if lit_état(animal) is not None:
        if lit_état(animal) != 'affamé':
            return 'Désolé, ' + str(animal.animal_name) + " n'a pas faim..."
            
        elif vérifie_disponibilité('mangeoire') != 'libre':
            occupant = cherche_occupant('mangeoire')
            return 'Désolé, la mangeoire est occupée par ' + str(occupant)
        else:
            change_état(animal, 'repus')
            change_lieu(animal, 'mangeoire')
            return None
    else:
        return "Désolé, " + str(animal.animal_name) + " n'est pas un animal connu"

def divertir(animal):
    if lit_état(animal) is not None:
        if lit_état(animal) != 'repus':
            return 'Désolé, ' + str(animal.animal_name) + " n'est pas en état de faire du sport."
            
        elif vérifie_disponibilité('roue') != 'libre':
            occupant = cherche_occupant('roue')
            return 'Désolé, la roue est occupée par ' + str(occupant)
        else:
            change_état(animal, 'fatigué')
            change_lieu(animal, 'roue')
            return None
    else:
        return "Désolé, " + str(animal.animal_name) + " n'est pas un animal connu"

def coucher(animal):
    if lit_état(animal) is not None:
        if lit_état(animal) != 'fatigué':
            return 'Désolé, ' + str(animal.animal_name) + " n'est pas fatigué."
            
        elif vérifie_disponibilité('nid') != 'libre':
            occupant = cherche_occupant('nid')
            return 'Désolé, le nid est occupé par ' + str(occupant)
        else:
            change_état(animal, 'endormi')
            change_lieu(animal, 'nid')
            return None
    else:
        return "Désolé, " + str(animal.animal_name) + " n'est pas un animal connu"

def réveiller(animal):
    if lit_état(animal) is not None:
        if lit_état(animal) != 'endormi':
            return 'Désolé, ' + str(animal.animal_name) + " ne dort pas."
        else:
            change_état(animal, 'affamé')
            change_lieu(animal, 'litière')
            return None
    else:
        return "Désolé, " + str(animal.animal_name) + " n'est pas un animal connu"