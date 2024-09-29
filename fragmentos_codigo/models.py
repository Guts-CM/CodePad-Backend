from django.db import models
from notas.models import Notas

# Create your models here.
class FragmentosCodigo(models.Model):
    fragmentos_codigo_id = models.BigAutoField(primary_key=True)
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE)
    contenido_codigo = models.TextField()
    lenguaje = models.CharField(max_length=40)
    orden_en_nota = models.IntegerField()

    class Meta:
        db_table = 'fragmentos_codigo'
        managed = False