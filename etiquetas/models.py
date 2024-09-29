from django.db import models

# Create your models here.
class Etiquetas(models.Model):
    etiquetas_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

    class Meta:
        db_table = 'etiquetas'
        managed = False