<?php
$destinataire = "destinataire@example.com";
$sujet = "Sujet de l'email";
$message = "Contenu de l'email";

// En-têtes de l'email
$headers = "From: expéditeur@example.com\r\n";
$headers .= "Reply-To: expéditeur@example.com\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";

// Envoyer l'email
if (mail($destinataire, $sujet, $message, $headers)) {
    echo "L'email a été envoyé avec succès.";
} else {
    echo "Erreur lors de l'envoi de l'email.";
}
?>
