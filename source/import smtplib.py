import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Paramètres de l'expéditeur
sender_email = "votre_email@gmail.com"
sender_password = "votre_mot_de_passe"

# Paramètres du destinataire
recipient_email = "email_du_destinataire@gmail.com"

# Créer un objet MIMEMultipart
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = "Sujet de l'e-mail"

# Corps du message
message.attach(MIMEText("Contenu de l'e-mail.", 'plain'))

# Vous pouvez également joindre des fichiers (facultatif)
# avec open('chemin_du_fichier', 'rb') as attachment:
#     part = MIMEApplication(attachment.read())
#     part.add_header('Content-Disposition', f'attachment; filename=nom_du_fichier')
#     message.attach(part)

# Se connecter au serveur SMTP de l'expéditeur (dans ce cas, Gmail)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# S'authentifier avec le compte expéditeur
server.login(sender_email, sender_password)

# Envoyer l'e-mail
text = message.as_string()
server.sendmail(sender_email, recipient_email, text)

# Fermer la connexion au serveur SMTP
server.quit()

print("E-mail envoyé avec succès !")
