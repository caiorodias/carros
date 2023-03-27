from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200) #maximo 200 caracteres
    brand = models.CharField(max_length=200) #marca
    factory_year = models.IntegerField(blank=True, null=True) #ano #o blank e o null como true, quer dizer que se quiser da pra deixar em branco, nesse caso só seriam obrigatorios o modelo e a marca.
    model_year = models.IntegerField(blank=True, null=True) #ano
    value = models.FloatField(blank=True, null=True) #ponto flutuante
    
    def __str__(self):
        return self.model #Troca o nome object no site admin pelo nome do item