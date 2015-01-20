<?php

require('config.inc.php');

session_start();

if (!isset($_POST['type']) or !isset($_POST['id'])) exit('Brak danych.');
if (!isset($_POST['offset'])) $_POST['offset'] = 10;


if ($_POST['type'] == 'normal')
{
  $data = file($log);
  $ile_linii = count($data);
  
  if ($_POST['lines'] == 0) $_SESSION[$_POST['id']]["log_normal_pobrano"] = 0;
  
  if (isset($_SESSION[$_POST['id']]["log_normal_pobrano"]) && ($_POST['lines'] != 0))
  {
    if ($ile_linii > $_SESSION[$_POST['id']]["log_normal_pobrano"])
    {
      $data = array_slice($data, $_SESSION[$_POST['id']]["log_normal_pobrano"] - $ile_linii);
      $_SESSION[$_POST['id']]["log_normal_pobrano"] = $ile_linii;
    }
    else
    {
      $data = array();
    }
  }
  else
  {
    $offset = $_POST['offset'] - 2 * $_POST['offset'];
    $data = array_slice($data, $offset);
    $_SESSION[$_POST['id']]["log_normal_pobrano"] = $ile_linii;
  }
}
else
{
  $data = @file($log_error);
  
  if (!$data) $data = array();
  
  $ile_linii = count($data);
  
  if ($_POST['lines'] == 0) $_SESSION[$_POST['id']]["log_error_pobrano"] = 0;
  
  if (isset($_SESSION[$_POST['id']]["log_error_pobrano"]) && ($_POST['lines'] != 0))
  {
    if ($ile_linii > $_SESSION[$_POST['id']]["log_error_pobrano"])
    {
      $data = array_slice($data, $_SESSION[$_POST['id']]["log_error_pobrano"] - $ile_linii);
      $_SESSION[$_POST['id']]["log_error_pobrano"] = $ile_linii;
    }
    else
    {
      $data = array();
    }
  }
  else
  {
    $offset = $_POST['offset'] - 2 * $_POST['offset'];
    $data = array_slice($data, $offset);
    $_SESSION[$_POST['id']]["log_error_pobrano"] = $ile_linii;
  }
}

foreach ($data as $line)
  echo nl2br($line, false);

?>
