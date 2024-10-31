from rest_framework import generics
from .models import Usuarios
from .serializers import UsuarioSerializer, CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate  

# Servicio para crear un nuevo usuario (POST)
class CrearUsuarioView(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

# Servicio para listar todos los usuarios y crear uno nuevo (GET y POST)
class ListarUsuariosView(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

# Servicio para obtener, actualizar o eliminar un usuario específico (GET, PUT, DELETE)
class DetalleUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

# Servicio para autenticar y obtener un token JWT personalizado
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
