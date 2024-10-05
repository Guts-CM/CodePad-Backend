from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuariosManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo username es obligatorio')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    usuarios_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)

    # Campos requeridos para usar AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuariosManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno', 'correo']

    # Añadir estos campos para evitar conflictos
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

    class Meta:
        db_table = 'usuarios'
        managed = True  # Cambia a True para permitir migraciones

    @property
    def id(self):
        return self.usuarios_id  # Devuelve el valor de usuarios_id como id
