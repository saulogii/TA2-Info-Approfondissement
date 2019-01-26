from django.db import models

# Create your models here.

class Etat(models.Model):
	etat_text = models.CharField(max_length=200)

	def __str__(self):
		return self.etat_text

class Lieu(models.Model):
	equipement_text = models.CharField(max_length=200) 
	disponibilite = models.CharField(max_length=200)

	def __str__(self):
		return self.equipement_text

class Animal(models.Model):
	lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
	etat = models.ForeignKey(Etat, on_delete=models.CASCADE)
	animal_name = models.CharField(max_length=200)
	animal_race = models.CharField(max_length=200)
	animal_type = models.CharField(max_length=200)

	def __str__(self):
		return self.animal_name

class Action(models.Model):
	action_text = models.CharField(max_length=200)

	def __str__(self):
		return self.action_text