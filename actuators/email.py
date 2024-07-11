import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

log = logging.getLogger(__name__)

def send_email(smtp_server, smtp_port, smtp_user, smtp_password, to_email, subject, body):
    try:
        # Crear el objeto del mensaje
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Agregar el cuerpo del mensaje
        msg.attach(MIMEText(body, 'plain'))
        
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Iniciar sesión en el servidor SMTP
        server.login(smtp_user, smtp_password)
        
        # Enviar el correo
        server.send_message(msg)
        
        # Cerrar la conexión al servidor SMTP
        server.quit()
        
        log.info(f"Email enviado a {to_email}")
    except Exception as e:
        log.error(f"Error enviando email: {e}")

# Ejemplo de uso:
# send_email('smtp.example.com', 587, 'tu_correo@example.com', 'tu_contraseña', 'destinatario@example.com', 'Asunto', 'Cuerpo del mensaje')
