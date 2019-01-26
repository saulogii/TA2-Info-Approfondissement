# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.template import loader
from .controle_view import *

latest_animal_list = Animal.objects.all()
latest_action_list = Action.objects.all()

def index(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_animal_list': latest_animal_list,
        'latest_action_list': latest_action_list,
    }
    return HttpResponse(template.render(context, request))

def changer(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    try:
        selected_animal = Animal.objects.get(pk=request.POST['anichoice'])
        selected_action = Action.objects.get(pk=request.POST['actchoice'])
    except (KeyError, Animal.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'latest_animal_list': latest_animal_list,
            'latest_action_list': latest_action_list,
            'error_message': "Vous n'avez pas selectionné un animal et une action!",
        })
    else:
        if selected_action.id == 1:
            reponse = nourrir(selected_animal)
        if selected_action.id == 2:
            reponse = divertir(selected_animal)
        if selected_action.id == 3:
            reponse = coucher(selected_animal)
        if selected_action.id == 4:
            reponse = réveiller(selected_animal)
        
        if reponse != None:
            return render(request, 'polls/index.html', {
            'latest_animal_list': latest_animal_list,
            'latest_action_list': latest_action_list,
            'error_message': reponse,
        })
            #return HttpResponse(reponse)

        return HttpResponseRedirect(reverse('polls:index'))

def detailretirer(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    return render(request, 'polls/retirer.html', {
        'latest_animal_list': latest_animal_list
        })

def retirer(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    try:
        selected_animal = Animal.objects.get(pk=request.POST['anichoice'])
    except (KeyError, Animal.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/retirer.html', {
            'latest_animal_list': latest_animal_list,
            'latest_action_list': latest_action_list,
            'error_message': "Vous n'avez pas selectionné un animal. Vous pouvez toujour canceler",
        })
    else:
        selected_lieu = selected_animal.lieu
        selected_lieu.disponibilite = 'libre' 
        selected_lieu.save()
        selected_animal.delete()

        return HttpResponseRedirect(reverse('polls:index'))

def detailajouter(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    return render(request, 'polls/ajouter.html', {
        'latest_animal_list': latest_animal_list
        })

def ajouter(request):
    latest_animal_list = Animal.objects.all()
    latest_action_list = Action.objects.all()
    lieu_first = Lieu.objects.get(equipement_text = 'litière')
    etat_first = Etat.objects.get(etat_text = 'affamé')
    try:
        animalname = request.POST['animalname']
        animalrace = request.POST['animalrace']
        animaltype = request.POST['animaltype']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'polls/ajouter.html', {
            'error_message': "Vous n'avez pas rempli le formulaire"
        })
    else:
        new_animal = Animal(lieu = lieu_first, 
            etat = etat_first,
            animal_name = animalname,
            animal_race = animalrace,
            animal_type = animaltype)

        new_animal.save()

        return HttpResponseRedirect(reverse('polls:index'))

'''
def index(request):
    latest_animal_list = Animal.objects.all()
    output = ', '.join([q.animal_name for q in latest_animal_list])
    return HttpResponse(output)
'''