from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuarios(models.Model):
    usuarios_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    nombres = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)
    pista_password = models.CharField(max_length=80)
    activo = models.BooleanField(null=True)
    fecha_creacion = models.DateTimeField()
    ultimo_acceso = models.DateTimeField(null=True)

    class Meta:
        db_table = 'usuarios'
        managed = False

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
