import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(to_email, subject, body, attachment_path):
    from_email = "facturadorapython@gmail.com"  # Cambia esto por tu correo
    from_password = "Facturadora.1"  # Cambia esto por tu contraseña

    # Configuración del correo
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Agregar cuerpo del correo
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo CSV
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.attach(part)

    # Enviar el correo
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
