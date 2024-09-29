from django.db import models
from notas.models import Notas
from usuarios.models import Usuarios

# Create your models here.
class CompartirNotas(models.Model):
    compartir_notas_id = models.BigAutoField(primary_key=True)
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE)
    usuario_origen = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='usuario_origen')
    usuario_destino = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, related_name='usuario_destino')
    permiso = models.BooleanField()
    fecha_compartido = models.DateTimeField()

    class Meta:
        db_table = 'compartir_notas'
        managed = False