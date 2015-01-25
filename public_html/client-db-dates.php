<?php

require_once('common.inc.php');
require_once('config.inc.php');


$query = "SELECT MIN(czas) AS czas_min, MAX(czas) AS czas_max FROM historia";

switch ($_POST['baza'])
{ 
  case 'mysql':
    $mysqli = new mysqli($db_mysql_host, $db_mysql_user, $db_mysql_pass, $db_mysql_name);

    if ($mysqli->connect_errno) {
        die("Błąd połączenia z bazą.\n");
    }

    $result = $mysqli->query($query);
    $row = $result->fetch_array(MYSQLI_ASSOC);    
    break;
  
  case 'sqlite':
    $db_sqlite = new MyDB($db_sqlite_path);
    $result = $db_sqlite->query($query);
    $row = $result->fetchArray(SQLITE3_ASSOC);    
    break;
  
  default:
    exit("Wystąpił błąd. \n");
}


// format odpowiedzi: 13;12;2014;22;59;22;01;2015;21;46

echo date("d", $row['czas_min']).';'.date("m", $row['czas_min'])
  .';'.date("Y", $row['czas_min']).';'.date("H", $row['czas_min'])
  .';'.date("i", $row['czas_min']).';';

echo date("d", $row['czas_max']).';'.date("m", $row['czas_max'])
  .';'.date("Y", $row['czas_max']).';'.date("H", $row['czas_max'])
  .';'.date("i", $row['czas_max']);


switch ($_POST['baza'])
{ 
  case 'mysql':
    $result->free();
    $mysqli->close(); 
    break;
  
  case 'sqlite':
    $db_sqlite->close();
    unset($db_sqlite); 
    break;
}

?>