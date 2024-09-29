from django.db import models
from notas.models import Notas

# Create your models here.
class VersionesNota(models.Model):
    versiones_nota_id = models.BigAutoField(primary_key=True)
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=75)
    fecha_version = models.DateTimeField()

    class Meta:
        db_table = 'versiones_nota'
        managed = False