<?php
require('config.inc.php');
?>

<div id="container">
  <h2>Statystyki pracy systemu</h2>
  <div id="oddo2">
    <form name="statystyki">
    <table>
      <tr>
        <td colspan="6">Baza danych: <select name="baza" onchange="GetDates(document.statystyki, 'cont_statystyki');">
            <option value=""></option>
            <?php if (!empty($db_mysql_name)) { ?><option value="mysql">MySQL</option><?php } ?>
            <?php if (!empty($db_sqlite_path)) { ?><option value="sqlite">SQLite</option><?php } ?>
          </select>
        </td>
      </tr>
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
