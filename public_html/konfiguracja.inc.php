<div id="container">
  <h2>Konfiguracja systemu</h2>
    <form name="konfiguracja">
    Opcja:<br />
    <select name="opcja" onchange="GetConfig(this);">
      <option value=""></option>
      <optgroup label="general">
        <option value="loglevel">loglevel</option>
        <option value="czujnik_temp">czujnik_temp</option>
        <option value="czujnik_temp_wew">czujnik_temp_wew</option>
        <option value="czujnik_temp_zew">czujnik_temp_zew</option>
        <option value="relay_on">relay_on</option>
        <option value="relay_off">relay_off</option>  
      </optgroup>
      <optgroup label="co">
        <option value="wlaczone">wlaczone</option>
        <option value="dioda">dioda</option>
        <option value="dioda">gpio</option>
        <option value="czas_probek_temp">czas_probek_temp</option>
        <option value="t_petli">t_petli</option>
        <option value="histereza">histereza</option>
        <option value="rozpalanie_delta">rozpalanie_delta</option>
        <option value="wygaszanie_delta">wygaszanie_delta</option>
        <option value="rozpalanie">rozpalanie</option>
        <option value="wygaszanie">wygaszanie</option>
        <option value="czujnik_temp_zasilania">czujnik_temp_zasilania</option>
        <option value="czujnik_temp_powrotu">czujnik_temp_powrotu</option>
        <option value="gdy_priorytet_cwu">gdy_priorytet_cwu</option>
        <option value="temp_alarm">temp_alarm</option>
        <option value="temp_alarm">temp_alarm</option>
        <option value="temp_rozpalanie">temp_rozpalanie</option>
        <option value="temp_wygaszanie">temp_wygaszanie</option>
        <option value="temp_start">temp_start</option>
        <option value="temp_min">temp_min</option>
      </optgroup>
      <optgroup label="cwu">
        <option value="wlaczone">wlaczone</option>
        <option value="dioda">dioda</option>
        <option value="dioda">gpio</option>
        <option value="czujnik_temp">czujnik_temp</option>
        <option value="t_petli">t_petli</option>
        <option value="gdy_rozpalanie">gdy_rozpalanie</option>
        <option value="priorytet">priorytet</option>
        <option value="temp_max">temp_max</option>
        <option value="temp_min_co">temp_min_co</option>
        <option value="temp_alarm">temp_alarm</option>
        <option value="histereza">histereza</option>
      </optgroup>
      <optgroup label="ogrzewanie_podlogowe">
        <option value="wlaczone">wlaczone</option>
        <option value="dioda">dioda</option>
        <option value="dioda">gpio</option>
        <option value="histereza">histereza</option>
        <option value="czujnik_temp">czujnik_temp</option>
        <option value="gdy_rozpalanie">gdy_rozpalanie</option>
        <option value="gdy_priorytet_cwu">gdy_priorytet_cwu</option>
        <option value="temp_min_co">temp_min_co</option>
        <option value="temp_alarm">temp_alarm</option>
        <option value="t_petli">t_petli</option>
      </optgroup>
      <optgroup label="cyrkulacja">
        <option value="wlaczone">wlaczone</option>
        <option value="dioda">dioda</option>
        <option value="dioda">gpio</option>
        <option value="manual">manual</option>
        <option value="histereza">histereza</option>
        <option value="czujnik_temp">czujnik_temp</option>
        <option value="t_petli">t_petli</option>
        <option value="harmonogram_wlaczony">harmonogram_wlaczony</option>
        <option value="harmonogram">harmonogram</option>
        <option value="temp_max">temp_max</option>
        <option value="temp_alarm">temp_alarm</option>
      </optgroup>
      <optgroup label="grzalka">
        <option value="wlaczone">wlaczone</option>
        <option value="dioda">dioda</option>
        <option value="dioda">gpio</option>
        <option value="t_petli">t_petli</option>
        <option value="temp_max">temp_max</option>
        <option value="gdy_cwu">gdy_cwu</option>
        <option value="gdy_co">gdy_co</option>
        <option value="manual">manual</option>
        <option value="harmonogram_wlaczony">harmonogram_wlaczony</option>
        <option value="harmonogram">harmonogram</option>
        <option value="histereza">histereza</option>
      </optgroup>
      <optgroup label="termopara">
        <option value="wlaczone">wlaczone</option>
        <option value="gpio_cs">gpio_cs</option>
        <option value="gpio_clock">gpio_clock</option>
        <option value="gpio_data">gpio_data</option>
        <option value="t_petli">t_petli</option>
        <option value="temp_alarm">temp_alarm</option>
        <option value="tylko_gdy_co">tylko_gdy_co</option>
      </optgroup>
      <optgroup label="mysql">
        <option value="wlaczone">wlaczone</option>
        <option value="user">user</option>
        <option value="pass">pass</option>
        <option value="db">db</option>
        <option value="host">host</option>
        <option value="freq_zapisu">freq_zapisu</option>
      </optgroup>
      <optgroup label="sqlite3">
        <option value="wlaczone">wlaczone</option>
        <option value="db">db</option>
        <option value="freq_zapisu">freq_zapisu</option>
      </optgroup>
    </select><br />Wartość:
    <input type="radio" name="TakNie1" value="True" onclick="TakNie(this);">Tak
    <input type="radio" name="TakNie1" value="False" onclick="TakNie(this);">Nie<br />
    <textarea name="wartosc" onchange="Zmiana(this);"></textarea><br />
    Hasło:<br /><input type="password" name="pass" value=""><br />
    </form><button id="zapisz" onclick="SendConfig();">Zapisz</button>
</div>
