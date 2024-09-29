# usuarios/urls.py
from django.urls import path
from .views import ListarUsuariosView, DetalleUsuarioView, LoginView  # Asegúrate de importar todas las vistas necesarias

urlpatterns = [
    path('', ListarUsuariosView.as_view(), name='listar-usuarios'),  # Listar usuarios y crear uno nuevo
    path('<int:pk>/', DetalleUsuarioView.as_view(), name='detalle-usuario'),  # Obtener, actualizar o eliminar un usuario
    path('login/', LoginView.as_view(), name='login'),  # Iniciar sesión (agrega la barra diagonal)
]
