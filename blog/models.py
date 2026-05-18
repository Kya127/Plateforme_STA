from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Note(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='notes/')
    date_entree = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.titre
