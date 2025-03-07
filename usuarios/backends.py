# usuarios/backends.py

from django.contrib.auth.backends import BaseBackend
from .models import Usuarios

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(username=username)
            if user.check_password(password):
                return user
        except Usuarios.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk=user_id)
        except Usuarios.DoesNotExist:
            return None
