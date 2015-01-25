<?php

error_reporting(E_ALL);

@require('config.inc.php');

if (empty($_POST['message'])) exit('ERROR1');

$message =  $_POST['message'];

$socket = @socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false)
  exit("ERROR2: ".socket_strerror(socket_last_error()));

$result = @socket_connect($socket, $address, $service_port);
if ($result === false)
  exit("ERROR3: ".socket_strerror(socket_last_error($socket)));


$out = '';

socket_write($socket, $message, strlen($message));

while ($out = socket_read($socket, 2048)) {
    echo $out;
}

socket_close($socket);

?>
