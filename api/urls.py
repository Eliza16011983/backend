from django.urls import path
from .views import UsuarioListCreateView

urlpatterns = [
    path('users/', UsuarioListCreateView.as_view(), name='users-list-create'),
]
