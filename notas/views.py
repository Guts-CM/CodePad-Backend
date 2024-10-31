from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Notas
from .serializers import NotasSerializer
from rest_framework.permissions import IsAuthenticated

# POST - Crea un nuevo registro.
class NotasCreateView(APIView):
    def post(self, request):
        serializer = NotasSerializer(data=request.data)  # Deserializa los datos entrantes
        if serializer.is_valid():  # Si los datos son válidos
            serializer.save()  # Guarda el objeto en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET - Obtener datos.
class NotasListView(APIView):
    def get(self, request):
        notas = Notas.objects.all()  # Recupera todas las notas
        serializer = NotasSerializer(notas, many=True)  # Serializa las notas
        return Response(serializer.data)

class NotasDetailView(APIView):
    def get(self, request, pk):
        nota = get_object_or_404(Notas, pk=pk)  # Maneja automáticamente el error 404 si no encuentra la nota
        serializer = NotasSerializer(nota)
        return Response(serializer.data)

# PUT - Actualizar registros.
class NotasUpdateView(APIView):
    def put(self, request, pk):
        nota = get_object_or_404(Notas, pk=pk)  # Busca o retorna un 404 si no existe
        serializer = NotasSerializer(nota, data=request.data)  # Deserializa y actualiza
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE - Eliminar registros.
class NotasDeleteView(APIView):
    def delete(self, request, pk):
        nota = get_object_or_404(Notas, pk=pk)  # Maneja automáticamente el error 404 si no encuentra la nota
        nota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
