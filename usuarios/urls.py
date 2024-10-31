# usuarios/urls.py
from django.urls import path
from .views import ListarUsuariosView, DetalleUsuarioView, CustomTokenObtainPairView

urlpatterns = [
    path('', ListarUsuariosView.as_view(), name='listar-usuarios'),  # Listar usuarios y crear uno nuevo
    path('<int:pk>/', DetalleUsuarioView.as_view(), name='detalle-usuario'),  # Obtener, actualizar o eliminar un usuario
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Iniciar sesión y obtener token
]
