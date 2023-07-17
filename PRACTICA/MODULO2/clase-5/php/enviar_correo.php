<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recuperar los valores del formulario
    $nombre = $_POST["nombre"];
    $correo = $_POST["correo"];
    $mensaje = $_POST["mensaje"];

    // Configurar los detalles del correo electrónico
    $destinatario = "jorgeangelpaez@gmail.com"; // Cambia esto con la dirección de correo a la que deseas enviar el mensaje
    $asunto = "Formulario de contacto - " . $nombre;
    $cuerpoMensaje = "Nombre: " . $nombre . "\n";
    $cuerpoMensaje .= "Correo electrónico: " . $correo . "\n";
    $cuerpoMensaje .= "Mensaje:\n" . $mensaje;

    // Enviar el correo electrónico
    if (mail($destinatario, $asunto, $cuerpoMensaje)) {
        echo "El mensaje se envió correctamente. Gracias por contactarnos.";
    } else {
        echo "Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.";
    }
}
?>
