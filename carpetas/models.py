from django.db import models
from usuarios.models import Usuarios

# Create your models here.
class Carpetas(models.Model):
    carpetas_id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=80, null=True)
    ico_url = models.CharField(max_length=40, null=True)
    carpeta_padre = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'carpetas'
        managed = False