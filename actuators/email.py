import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

log = logging.getLogger(__name__)

def send_email(text:str):
    
    try:
        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = 'javierfernandezbarreiro@gmail.com'
        mensaje['To'] = 'javierfernandezbarreiro@gmail.com'
        mensaje['Subject'] = "Greengarden cambio IP local"

        # Adjuntar contenido HTML
        mensaje.attach(MIMEText(text, 'plain'))

        # Conectar al servidor SMTP y enviar correo
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('javierfernandezbarreiro@gmail.com', '***')
            server.sendmail('javierfernandezbarreiro@gmail.com', 'javierfernandezbarreiro@gmail.com', mensaje.as_string())

    except Exception as e:
        print('Error al enviar el correo.' + e)

