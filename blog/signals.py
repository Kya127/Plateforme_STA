from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Note

@receiver(post_save,sender=Note)
def Notification(sender,instance,created,**kwargs):
    auteur = instance.auteur.username
    if created:
        print(f"[Alerte]:{auteur} a crée une note {instance.titre}.")
    else:
        print(f"[Alerte]:{auteur} a modifié {instance.titre}.")    
