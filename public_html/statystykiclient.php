<?php

require('config.inc.php');


function Czas ($sekund)
{
  if ($sekund >= 3600) {
    $sekund /= 3600;
    $sekund = round($sekund, 1);
    $sekund .= ' h';
  }
  elseif ($sekund >= 60) {
    $sekund /= 60;
    $sekund = round($sekund, 1);
    $sekund .= ' min';
  } else {
    $sekund = round($sekund, 1);
    $sekund .= ' s';
  }
  
  return $sekund;
}

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);


if ($mysqli->connect_errno) {
    die("Connect failed: \n");
}

$czas_od = strtotime($_POST['od_dzien'].'-'.$_POST['od_miesiac']
  .'-'.$_POST['od_rok'].' '.$_POST['od_godzina'].':'.$_POST['od_minuta']);
  
$czas_do = strtotime($_POST['do_dzien'].'-'.$_POST['do_miesiac'].'-'
  .$_POST['do_rok'].' '.$_POST['do_godzina'].':'.$_POST['do_minuta']);

$stats = array();

$query = 'SELECT '
  .'SUM(trwanie) AS suma_trwanie, '
  /*.'AVG(co_temp_zasilania) AS srednia_co_temp_zasilania, '
  .'MIN(co_temp_zasilania) AS min_co_temp_zasilania, '
  .'MAX(co_temp_zasilania) AS max_co_temp_zasilania, '
  .'AVG(co_temp_powrotu) AS srednia_co_temp_powrotu, '
  .'MIN(co_temp_powrotu) AS min_co_temp_powrotu, '
  .'MAX(co_temp_powrotu) AS max_co_temp_powrotu, '*/
  .'AVG(cwu_temp) AS srednia_cwu_temp, '
  .'MIN(cwu_temp) AS min_cwu_temp, '
  .'MAX(cwu_temp) AS max_cwu_temp, '
  /*.'AVG(ogrzewanie_podlogowe_temp) AS srednia_ogrzewanie_podlogowe_temp, '
  .'MIN(ogrzewanie_podlogowe_temp) AS min_ogrzewanie_podlogowe_temp, '
  .'MAX(ogrzewanie_podlogowe_temp) AS max_ogrzewanie_podlogowe_temp, '*/
  .'AVG(cyrkulacja_temp) AS srednia_cyrkulacja_temp, '
  .'MIN(cyrkulacja_temp) AS min_cyrkulacja_temp, '
  .'MAX(cyrkulacja_temp) AS max_cyrkulacja_temp, ' 
  .'AVG(temp) AS srednia_temp, '
  .'MIN(temp) AS min_temp, '
  .'MAX(temp) AS max_temp, '   
  .'AVG(temp_wew) AS srednia_temp_wew, '
  .'MIN(temp_wew) AS min_temp_wew, '
  .'MAX(temp_wew) AS max_temp_wew, '    
  .'AVG(temp_zew) AS srednia_temp_zew, '
  .'MIN(temp_zew) AS min_temp_zew, '
  .'MAX(temp_zew) AS max_temp_zew, '
  .'MAX(termopara_temp) AS max_termopara_temp '  
  .'FROM historia WHERE czas>='.$czas_od.' AND czas<='.$czas_do;

$result = $mysqli->query($query);
$stats = $result->fetch_array(MYSQLI_ASSOC);
$result->free();

$query = 'SELECT '
  .'AVG(co_temp_zasilania) AS srednia_co_temp_zasilania, '
  .'MIN(co_temp_zasilania) AS min_co_temp_zasilania, '
  .'MAX(co_temp_zasilania) AS max_co_temp_zasilania, '
  .'AVG(co_temp_powrotu) AS srednia_co_temp_powrotu, '
  .'MIN(co_temp_powrotu) AS min_co_temp_powrotu, '
  .'MAX(co_temp_powrotu) AS max_co_temp_powrotu, '
  .'MIN(termopara_temp) AS min_termopara_temp, '
  .'AVG(termopara_temp) AS srednia_termopara_temp '
  .'FROM historia '
  .'WHERE co_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do;
  
$result = $mysqli->query($query);
$stats = array_merge($stats, $result->fetch_array(MYSQLI_ASSOC));
$result->free();
  
$query = 'SELECT '
  .'AVG(ogrzewanie_podlogowe_temp) AS srednia_ogrzewanie_podlogowe_temp, '
  .'MIN(ogrzewanie_podlogowe_temp) AS min_ogrzewanie_podlogowe_temp, '
  .'MAX(ogrzewanie_podlogowe_temp) AS max_ogrzewanie_podlogowe_temp '
  .'FROM historia '
  .'WHERE ogrzewanie_podlogowe_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do;
  
$result = $mysqli->query($query);
$stats = array_merge($stats, $result->fetch_array(MYSQLI_ASSOC));
$result->free();

$query  = 'SELECT SUM(trwanie) AS suma_trwanie_co_praca FROM historia WHERE co_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_trwanie_co_rozpalanie FROM historia WHERE co_rozpalanie=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_trwanie_co_wygaszanie FROM historia WHERE co_wygaszanie=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_trwanie_cwu_praca FROM historia WHERE cwu_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_trwanie_ogrzewanie_podlogowe_praca FROM historia WHERE ogrzewanie_podlogowe_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_trwanie_cyrkulacja_praca FROM historia WHERE cyrkulacja_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do.';'
  .'SELECT SUM(trwanie) AS suma_grzalka_praca FROM historia WHERE grzalka_praca=1 AND czas>='.$czas_od.' AND czas<='.$czas_do;

if ($mysqli->multi_query($query)) {
    do {
        if ($result = $mysqli->store_result()) {
            while ($row = $result->fetch_array(MYSQLI_BOTH)) {
                if ($row[0] === NULL) $row[0] = 0;
                $stats[array_keys($row, $row[0])[1]] = $row[0];
            }
            $result->free();
        }
    } while ($mysqli->next_result());
}

$mysqli->close(); 

/*
$stats['suma_trwanie'] => 19620
$stats['srednia_co_temp_zasilania'] => 35.800000
$stats['min_co_temp_zasilania'] => 27.25
$stats['max_co_temp_zasilania'] => 51.69
$stats['srednia_co_temp_powrotu'] => 33.692966
$stats['min_co_temp_powrotu'] => 26.62
$stats['max_co_temp_powrotu'] => 45.00
$stats['srednia_cwu_temp'] => 39.449083
$stats['min_cwu_temp'] => 22.31
$stats['max_cwu_temp'] => 47.56
$stats['srednia_ogrzewanie_podlogowe_temp'] => 29.882079
$stats['min_ogrzewanie_podlogowe_temp'] => 26.50
$stats['max_ogrzewanie_podlogowe_temp'] => 32.88
$stats['srednia_cyrkulacja_temp'] => 23.555015
$stats['min_cyrkulacja_temp'] => 21.88
$stats['max_cyrkulacja_temp'] => 24.94
$stats['suma_trwanie_co_praca'] => 19560
$stats['suma_trwanie_co_rozpalanie'] => 0
$stats['suma_trwanie_co_wygaszanie'] => 0
$stats['suma_trwanie_cwu_praca'] => 4200
$stats['suma_trwanie_ogrzewanie_podlogowe_praca'] => 19620
$stats['suma_trwanie_cyrkulacja_praca'] => 0
$stats['suma_grzalka_praca'] => 0
*/
?>

<table cellspacing="0" cellpadding="0">
<tr>
  <th rowspan="2">System</th>
  <td>czas pracy</td>
  <td class="wartosci"><?php echo Czas($stats['suma_trwanie']); ?></td>
</tr>
<tr>
  <td>temp. śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_temp'], 1).' /'.round($stats['min_temp'], 1).' /'.round($stats['max_temp'], 1); ?></td>
</tr>

<tr>
  <th rowspan="2">Warunki</th>
  <td>w domu śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_temp_wew'], 1).' /'.round($stats['min_temp_wew'], 1).' /'.round($stats['max_temp_wew'], 1); ?></td>
</tr>
<tr>
  <td>na zewnątrz śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_temp_zew'], 1).' /'.round($stats['min_temp_zew'], 1).' /'.round($stats['max_temp_zew'], 1); ?></td>
</tr>

<tr>
  <th rowspan="4">CO</th>
  <td>temp. zasilania śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_co_temp_zasilania'], 1).' /'.round($stats['min_co_temp_zasilania'], 1).' /'.round($stats['max_co_temp_zasilania'], 1); ?></td>
</tr>
<tr>
  <td>temp. powrotu śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_co_temp_powrotu'], 1).' /'.round($stats['min_co_temp_powrotu'], 1).' /'.round($stats['max_co_temp_powrotu'], 1); ?></td>
</tr>
<tr>
  <td>czas pracy obieg /rozpalanie /wygaszanie</td>
  <td class="wartosci"><?php echo Czas($stats['suma_trwanie_co_praca']).' /'.Czas($stats['suma_trwanie_co_rozpalanie']).' /'.Czas($stats['suma_trwanie_co_wygaszanie']); ?></td>
</tr>
<tr>
  <td>temp. spalin śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_termopara_temp'], 1).' /'.round($stats['min_termopara_temp'], 1).' /'.round($stats['max_termopara_temp'], 1); ?></td>
</tr>

<tr>
  <th rowspan="2">CWU</th>
  <td>temp. śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_cwu_temp'], 1).' /'.round($stats['min_cwu_temp'], 1).' /'.round($stats['max_cwu_temp'], 1); ?></td>
</tr>
<tr>
  <td>czas pracy</td>
  <td class="wartosci"><?php echo Czas($stats['suma_trwanie_cwu_praca']); ?></td>
</tr>


<tr>
  <th rowspan="2">Ogrzewanie podłogowe</th>
  <td>temp. śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_ogrzewanie_podlogowe_temp'], 1).' /'.round($stats['min_ogrzewanie_podlogowe_temp'], 1).' /'.round($stats['max_ogrzewanie_podlogowe_temp'], 1); ?></td>
</tr>
<tr>
  <td>czas pracy</td>
  <td class="wartosci"><?php echo Czas($stats['suma_trwanie_ogrzewanie_podlogowe_praca']); ?></td>
</tr>

<tr>
  <th rowspan="2">Cyrkulacja CWU</th>
  <td>temp. śr. /min /maks. [&degC]</td>
  <td class="wartosci"><?php echo round($stats['srednia_cyrkulacja_temp'], 1).' /'.round($stats['min_cyrkulacja_temp'], 1).' /'.round($stats['max_cyrkulacja_temp'], 1); ?></td>
</tr>
<tr>
  <td>czas pracy</td>
  <td class="wartosci"><?php echo Czas($stats['suma_trwanie_cyrkulacja_praca']); ?></td>
</tr>

<tr>
  <th>Grzałka</th>
  <td>czas pracy</td>
  <td class="wartosci"><?php echo Czas($stats['suma_grzalka_praca']); ?></td>
</tr>

</table>
