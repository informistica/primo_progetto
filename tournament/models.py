from django.db import models

class Squadre (models.Model):
    nome = models.CharField(max_length= 200)
    livello = models.IntegerField(default=0)
    nazione = models.CharField(max_length= 200)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= "Squadra"
        verbose_name_plural= "Squadre"

class Tornei (models.Model):
    nome = models.CharField(max_length= 200)
    squadre = models.ManyToManyField(Squadre, related_name = 'partecipanti')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= "Torneo"
        verbose_name_plural= "Tornei"