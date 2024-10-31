from rest_framework import serializers
from .models import Usuarios
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

    def validate_password(self, value):
        # Establece un límite de longitud para la contraseña
        if len(value) > 60:
            raise serializers.ValidationError("La contraseña no puede tener más de 60 caracteres.")
        return value

    def create(self, validated_data):
        # Crear el usuario sin encriptar la contraseña
        user = Usuarios(**validated_data)
        # Encriptar la contraseña
        user.set_password(validated_data['password'])
        user.save()
        return user

# Serializador personalizado para el token
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega el campo usuarios_id en lugar de user_id
        token['usuarios_id'] = user.usuarios_id

        # Elimina el campo user_id
        if 'user_id' in token:
            del token['user_id']

        return token