# notifications.py
import threading
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

def send_user_created_email(user):
    """
    Envía un correo de notificación al admin cuando se crea un nuevo usuario.
    Se ejecuta en segundo plano para no bloquear la API.
    """
    def _send_email():
        subject = 'Nuevo usuario creado'
        message = (
            f'Se ha creado un nuevo usuario:\n\n'
            f'Nombre: {user.nombre}\n'
            f'Email: {user.email}\n'
            f'Teléfono: {user.telefono}'
        )
        recipient_list = [settings.ADMIN_EMAIL]  # correo del admin
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # remitente
                recipient_list,
                fail_silently=False,
            )
            print(f"Notificación enviada a {recipient_list}")
        except BadHeaderError:
            print("Error: encabezado inválido en el correo")
        except Exception as e:
            print(f"Error al enviar correo: {e}")

    # Ejecuta el envío en un hilo separado
    threading.Thread(target=_send_email).start()
