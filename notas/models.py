from django.db import models
from usuarios.models import Usuarios
from etiquetas.models import Etiquetas

# Create your models here.
class Notas(models.Model):
    notas_id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiquetas, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=90)
    contenido = models.TextField(null=True)
    img_url = models.CharField(max_length=120, null=True)
    es_favorita = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(null=True)

    class Meta:
        db_table = 'notas'
        managed = False