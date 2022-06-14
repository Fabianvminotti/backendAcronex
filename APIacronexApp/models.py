#Modelos para registrar en la base de datos
from django.db import models

class maquinas(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    estado = models.CharField(max_length=4) #Estado de funcionamiento: alta/baja

def _str_(self):
        return self.id