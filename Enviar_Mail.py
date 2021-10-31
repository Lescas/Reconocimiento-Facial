# librerias
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# mensaje
msg = MIMEMultipart()
mensaje = "ejemplo 01"

# usuario y contraseña
contraseña = "Luanmaproyecto2021"
msg['From'] = "Luanma.tienda@gmail.com"
msg['To'] = "lucasbelgranoo@gmail.com"
msg['Subject'] = "Registro de Actividad"

# cuerpo del mensaje
msg.attach(MIMEText(mensaje, 'plain'))

#crear servidor
servidor = smtplib.SMTP('smtp.gmail.com: 587')

servidor.starttls()

# iniciar sesion
servidor.login(msg['From'], contraseña)


# enviar mensaje
servidor.sendmail(msg['From'], msg['To'], msg.as_string())

servidor.quit()

print ("correo enviado con exito a %s:" % (msg['To']))