from rest_framework import serializers
from .models import Usuarios

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