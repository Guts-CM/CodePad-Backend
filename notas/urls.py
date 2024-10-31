from django.urls import path
from .views import NotasCreateView, NotasListView, NotasDetailView, NotasUpdateView, NotasDeleteView

urlpatterns = [
    path('notas/', NotasListView.as_view(), name='notas-list'),  # Listar todas las notas
    path('notas/create/', NotasCreateView.as_view(), name='notas-create'),  # Crear una nueva nota
    path('notas/<int:pk>/', NotasDetailView.as_view(), name='notas-detail'),  # Obtener una nota por ID
    path('notas/<int:pk>/update/', NotasUpdateView.as_view(), name='notas-update'),  # Actualizar una nota
    path('notas/<int:pk>/delete/', NotasDeleteView.as_view(), name='notas-delete'),  # Eliminar una nota
]
