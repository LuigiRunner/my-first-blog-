from django.db import models

# Create your models here.

class AffairesSansRelation(models.Model):
    NomPrenomLeader = models.CharField(max_length=200)
    NumeroChantier = models.IntegerField()
    NbreLogements = models.IntegerField()
    DateFinChantier = models.DateTimeField()
    MarcheChantier = models.CharField(max_length=40)
    TypeChantier = models.CharField(max_length=40)
    StatutChantier = models.CharField(max_length=40)
        
    class Meta:
        verbose_name = "affaires sans relation"
        ordering = ['DateFinChantier']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.NumeroChantier