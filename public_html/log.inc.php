<div id="container">
  <h2>Dzienniki</h2>
  <div id="dzienniki_form">
    <form name="dzienniki" action="index.php?site=dzienniki">
    <table  cellspacing="0" cellpadding="0">
      <tr>
        <td>Dziennik pracy:</td><td><input type="checkbox" name="normal" value="true" /></td><td>rekordów z historii:</td><td><select name="snormal">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
            <option value="100">200</option>
            <option value="100">500</option>
            <option value="100">1000</option>
          </select></td>
      </tr>
      <tr>
        <td>Dziennik błędów:</td><td><input type="checkbox" name="error" value="true" /></td><td>rekordów z historii:</td><td><select name="serror">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
            <option value="100">200</option>
            <option value="100">500</option>
            <option value="100">1000</option>
          </select></td>
      </tr>
      <tr>
        <td>Obserwuj:</td><td><input type="checkbox" name="obserwuj" value="true" /></td><td colspan="2"><button onclick="GetLogs();return false;">Pobierz dzienniki</button></td>
      </tr>
    </table>
    </form>
  </div>
</div>
<div id="container_log_normal">
  <h3>Dziennik pracy:</h3>
  <div id="cont_log_normal"></div>
</div>
<div id="container_log_error">
  <h3>Dziennik błędów:</h3>
  <div id="cont_log_error"></div>
</div>