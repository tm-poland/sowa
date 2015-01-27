<?php

require_once('common.inc.php');
require_once('config.inc.php');

$time_start = microtime(true);

if (empty($_POST['wynikow'])) $_POST['wynikow'] = 20;
if (empty($_POST['start'])) $_POST['start'] = 0;

$czas_od = strtotime($_POST['od_dzien'].'-'.$_POST['od_miesiac']
  .'-'.$_POST['od_rok'].' '.$_POST['od_godzina'].':'.$_POST['od_minuta']);
  
$czas_do = strtotime($_POST['do_dzien'].'-'.$_POST['do_miesiac'].'-'
  .$_POST['do_rok'].' '.$_POST['do_godzina'].':'.$_POST['do_minuta'].':59');


switch ($_POST['baza'])
{ 
  case 'mysql':
  
    $mysqli = new mysqli($db_mysql_host, $db_mysql_user, $db_mysql_pass, $db_mysql_name);


    if ($mysqli->connect_errno) {
        die("Connect failed: \n");
    }
    
    $query = 'SELECT count(*) FROM historia WHERE czas>='.$czas_od.' AND czas<='.$czas_do;
    $result = $mysqli->query($query);
    $ile = $result->fetch_array(MYSQLI_NUM)[0];

    $query = 'SELECT * FROM historia WHERE czas>='.$czas_od.' AND czas<='.$czas_do
      .' ORDER by czas LIMIT '.$_POST['start'].', '.$_POST['wynikow'];
    $result = $mysqli->query($query);
    
    $num_rows = $result->num_rows;
    
    break;
  
  case 'sqlite':
    $db_sqlite = new MyDB($db_sqlite_path);
    
    $query = 'SELECT count(*) FROM historia WHERE czas>='.$czas_od.' AND czas<='.$czas_do;
    $result = $db_sqlite->query($query);
    $ile = $result->fetchArray(SQLITE3_NUM)[0];
    
    $query = 'SELECT * FROM historia WHERE czas>='.$czas_od.' AND czas<='.$czas_do
      .' ORDER by czas LIMIT '.$_POST['start'].', '.$_POST['wynikow'];

    $result = $db_sqlite->query($query);
    
    // test czy są wyniki  
    if ($result->fetchArray()[0] == null) {
      $num_rows = 0;
    } else {
      $num_rows = 1;
    } 
    
    break;
  
  default:
    exit("Wystąpił błąd. \n");
}
  
if ($num_rows > 0)
{
//$row = $result->fetch_array(MYSQLI_ASSOC);
  //echo '<table border="1">';
  ?>
  <table cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="9">
    <?php
    if ($_POST['start'] > 0)
    {
      echo '<button onclick="GetHistoria('
        .($_POST['start']-$_POST['wynikow']).', '.$_POST['wynikow']
        .');return false;"><<</button>';
    }
    ?>
      </td>
      <td colspan="9">
    <?php
    if (($_POST['start']+$_POST['wynikow']) < $ile)
    {
      echo '<button onclick="GetHistoria('.($_POST['start']+$_POST['wynikow'])
        .', '.$_POST['wynikow'].');return false;">>></button>';
    }
    ?>
    </td>
  </tr>
  <tr>
    <th>Data odczytu</th>
    <th>Interwał</th>
    <th>Praca CO</th>
    <th>Rozpa lanie kotła</th>
    <th>Wyga szanie kotła</th>
    <th>Temp. zas. CO [&degC]</th>
    <th>Temp. pow. CO [&degC]</th>
    <th>Praca CWU</th>
    <th>Temp. CWU [&degC]</th>
    <th>Praca OP</th>
    <th>Temp. OP [&degC]</th>
    <th>Praca cCWU</th>
    <th>Temp. cCWU [&degC]</th>
    <th>Praca grzałki</th>
    <th>Temp. sys. [&degC]</th>
    <th>Temp. wew. [&degC]</th>
    <th>Temp. zew. [&degC]</th>
    <th>Temp. spalin [&degC]</th>
  </tr>
  <?php
  
  $tr = 0;
  
  while ($row = ($_POST['baza'] == 'mysql'?$result->fetch_array(MYSQLI_ASSOC):$result->fetchArray(SQLITE3_ASSOC))) 
  {

    echo '<tr class="tr'.$tr.'">'
      .'<td>'.date("d-m-Y H:i:s", $row['czas']).'</td>'
      .'<td>'.Czas($row['trwanie']).'</td>'
      .'<td>'.($row['co_praca']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.($row['co_rozpalanie']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.($row['co_wygaszanie']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.$row['co_temp_zasilania'].'</td>'
      .'<td>'.$row['co_temp_powrotu'].'</td>'
      .'<td>'.($row['cwu_praca']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.$row['cwu_temp'].'</td>'
      .'<td>'.($row['ogrzewanie_podlogowe_praca']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.$row['ogrzewanie_podlogowe_temp'].'</td>'
      .'<td>'.($row['cyrkulacja_praca']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.$row['cyrkulacja_temp'].'</td>'
      .'<td>'.($row['grzalka_praca']=='1'?'Tak':'Nie').'</td>'
      .'<td>'.$row['temp'].'</td>'
      .'<td>'.$row['temp_wew'].'</td>'
      .'<td>'.$row['temp_zew'].'</td>'
      .'<td>'.$row['termopara_temp'].'</td>'
      .'</tr>';
      
    if ($tr > 0) $tr--;
    else $tr ++;
  }

  ?>
  <tr>
    <td colspan="9">
  <?php
  if ($_POST['start'] > 0)
  {
    echo '<button onclick="GetHistoria('
      .($_POST['start']-$_POST['wynikow']).', '.$_POST['wynikow']
      .');return false;"><<</button>';
  }
  ?>
    </td>
    <td colspan="9">
  <?php
  if (($_POST['start']+$_POST['wynikow']) < $ile)
  {
    echo '<button onclick="GetHistoria('.($_POST['start']+$_POST['wynikow'])
      .', '.$_POST['wynikow'].');return false;">>></button>';
  }
  ?>
    </td>
  </tr>
  </table>
  <?php
}
else
{
  echo 'Brak wyników.';
}


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

echo '<br />Wygenerowano w czasie '.round((microtime(true) - $time_start), 2).' s';

?>
