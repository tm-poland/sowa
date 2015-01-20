<?php
require('config.inc.php');
?>

<div id="container">
  <h2>Statystyki pracy systemu</h2>
  <div id="oddo2">
    <form name="statystyki">
    <table>
      <tr>
        <td></td>
        <td>Dzień:</td>
        <td>Miesiąc:</td>
        <td>Rok:</td>
        <td>Godzina:</td>
        <td>Minuta:</td>
      </tr>
      <tr>
        <td>Od:</td>
        <td><input type="text" name="od_dzien" value="" /></td>
        <td>
          <select name="od_miesiac">
            <option value="1">styczeń</option>
            <option value="2">luty</option>
            <option value="3">marzec</option>
            <option value="4">kwiecień</option>
            <option value="5">maj</option>
            <option value="6">czerwiec</option>
            <option value="7">lipiec</option>
            <option value="8">sierpień</option>
            <option value="9">wrzesień</option>
            <option value="10">październik</option>
            <option value="11">listopad</option>
            <option value="12">grudzień</option>
          </select>
        </td>
        <td><input type="text" name="od_rok" value="" /></td>
        <td><input type="text" name="od_godzina" value="" /></td>
        <td><input type="text" name="od_minuta" value="" /></td>
      </tr>
      <tr>
        <td>Do:</td>
        <td><input type="text" name="do_dzien" value="" /></td>
        <td>
          <select name="do_miesiac">
            <option value="1">styczeń</option>
            <option value="2">luty</option>
            <option value="3">marzec</option>
            <option value="4">kwiecień</option>
            <option value="5">maj</option>
            <option value="6">czerwiec</option>
            <option value="7">lipiec</option>
            <option value="8">sierpień</option>
            <option value="9">wrzesień</option>
            <option value="10">październik</option>
            <option value="11">listopad</option>
            <option value="12">grudzień</option>
          </select>
        </td>
        <td><input type="text" name="do_rok" value="" /></td>
        <td><input type="text" name="do_godzina" value="" /></td>
        <td><input type="text" name="do_minuta" value="" /></td>
      </tr>
      <tr>
        <td></td><td colspan="5"><button onclick="GetStatystyki();return false;">Pobierz statystyki</button></td>
      </tr>
    </table>
    </form>
  </div>
</div>
<div id="cont_statystyki"></div>
<?php

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);


if ($mysqli->connect_errno) {
    die("Błąd połączenia z bazą.\n");
}


$query = "SELECT * FROM historia ORDER by czas LIMIT 1";
$result = $mysqli->query($query);
$row = $result->fetch_array(MYSQLI_ASSOC);
?>
<script type="text/javascript">
//<![CDATA[
var obj = document.statystyki;

obj.od_dzien.value = "<?php echo date("d", $row['czas']); ?>";
obj.od_miesiac.value = "<?php echo date("m", $row['czas']); ?>";
obj.od_rok.value = "<?php echo date("Y", $row['czas']); ?>";
obj.od_godzina.value = "<?php echo date("H", $row['czas']); ?>";
obj.od_minuta.value = "<?php echo date("i", $row['czas']); ?>";

//]]>
</script>
<?php

$query = "SELECT * FROM historia ORDER by czas DESC LIMIT 1";
$result = $mysqli->query($query);
$row = $result->fetch_array(MYSQLI_ASSOC);

?>
<script type="text/javascript">
//<![CDATA[
var obj = document.statystyki;

obj.do_dzien.value = "<?php echo date("d", $row['czas']); ?>";
obj.do_miesiac.value = "<?php echo date("m", $row['czas']); ?>";
obj.do_rok.value = "<?php echo date("Y", $row['czas']); ?>";
obj.do_godzina.value = "<?php echo date("H", $row['czas']); ?>";
obj.do_minuta.value = "<?php echo date("i", $row['czas']); ?>";

//]]>
</script>
  
<?php 
$result->free();
$mysqli->close(); 
?>
