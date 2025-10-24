from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from .notifications import send_user_created_email


class UsuarioListCreateView(generics.ListCreateAPIView):
    """
    API REST que permite listar y crear usuarios.
    Al crear un usuario, se envía un correo de notificación.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        # Guardar el nuevo usuario en la base de datos
        user = serializer.save()
        # Enviar notificación por correo
        send_user_created_email(user)
