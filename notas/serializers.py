from rest_framework import serializers
from .models import Notas  # Importamos el modelo Notas que vamos a serializar

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas  # Especificamos el modelo que este serializador manejará
        fields = '__all__'  # Aquí indicamos que queremos serializar todos los campos del modelo
