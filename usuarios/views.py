from rest_framework import generics
from .models import Usuarios
from .serializers import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate  # Asegúrate de importar authenticate

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

# Servicio para iniciar sesión (POST)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)  # Usar authenticate

        if user is not None:
            # Generar un token JWT
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)
