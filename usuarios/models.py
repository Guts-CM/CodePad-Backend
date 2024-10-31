from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuariosManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo username es obligatorio')
        if not password:
            raise ValueError('El campo password es obligatorio')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Establece el password utilizando hashing
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Establece que es superusuario
        extra_fields.setdefault('is_superuser', True)  # Establece que es superusuario
        return self.create_user(username, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    usuarios_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    pista_password = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)

    objects = UsuariosManager()

    # Campos para relaciones con grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_set',  # Cambiar el nombre del grupo relacionado
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_set',  # Cambiar el nombre del permiso relacionado
        blank=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno', 'correo', 'pista_password']

    class Meta:
        db_table = 'usuarios'
        managed = True  # Cambia a True para permitir migraciones

    @property
    def id(self):
        return self.usuarios_id  # Devuelve el valor de usuarios_id como id
