<div id="container">

  <div id="inter">
    <img src="img/dom.png" alt="Wewnątrz" />
    <span id="general_temp_wew"></span>
  </div>
  
  <div id="outer">
    <img src="img/pogoda.png" alt="Na zewnątrz" />
    <span id="general_temp_zew"></span>
  </div>
  
  
  <h2>Stan systemu</h2>
  
  <div id="serwer">
    <div class="cont2">
      <h2 class="stan">Serwer</h2>
      <div class="temp">
        <span id="general_temp"></span>
      </div>
      <div id="error"></div>
    </div>
  </div>
  
  <div id="co">
    <div class="cont2">
      <h2 class="stan">CO</h2>
      <div class="temp">
        <span id="co_temp_zasilania"></span><br />
        <span id="co_temp_powrotu"></span><br />
        <span id="co_temp_spalin"></span>
      </div>  
      <p>Główny obieg centralnego ogrzewania dostarczający "ciepło" do grzejników. Główna wartość to temperatura na wyjściu z pieca CO, dolna dotyczy powrotu z grzejników i tym samym wejścia do kotła. Ostatnia wartość to temperatura spalin lub czopucha.</p>
    </div>
  </div>
  
  
  <div id="cwu">
    <div class="cont2">
      <h2 class="stan">CWU</h2>
      <div class="temp">
        <span id="grzalka_praca"></span>
        <span id="cwu_temp"></span><br />
        <span id="cyrkulacja_praca"></span>
        <span id="cyrkulacja_temp"></span>
      </div>
      <p>Nagrzewanie wody dostarczanej do punktów poboru (np. kran). Podana wartość dotyczy temperatury wody w zbiorniku (bojlerze). Dolne wartości określają obieg cyrkulacji ciepłej wody użytkowej w pobliżu punktów poboru.</p>
    </div>
  </div>
  
  <div id="ogrzewanie_podlogowe">
    <div class="cont2">
      <h2 class="stan">Ogrzewanie podłogowe</h2>
      <div class="temp">
        <span id="ogrzewanie_podlogowe_temp"></span>
      </div>
      <p>Obieg odpowiedzialny za nagrzewanie podłogi. Temperatura dotyczy zasilania obiegu.</p>
    </div>
  </div>

  <div id="legenda">
    <div class="cont2">
      <h3 class="stan">Legenda</h3>
      <table class="legenda">
      <tr><td class="kolory" style="background-color:white;">&nbsp;</td><td>opcja włączona</td></tr>
      <tr><td class="kolory" style="background-color:#cacaca;">&nbsp;</td><td>opcja wyłączona</td></tr>
      <tr><td class="kolory" style="background-color:#66CC00;">&nbsp;</td><td>praca obiegu</td></tr>
      <tr><td class="kolory" style="background-color:#ff6666;">&nbsp;</td><td>tryb rozpalania obiegu CO</td></tr>
      <tr><td class="kolory" style="background-color:#66ccff;">&nbsp;</td><td>tryb wygaszania obiegu CO</td></tr>
      <tr><td class="spirala"><img class="spirala" src="img/spirala_szara.png" alt="" /></td><td>opcja grzałki wyłączona</td></tr>
      <tr><td class="spirala"><img class="spirala" src="img/spirala_czarna.png" alt="" /></td><td>opcja grzałki włączona</td></tr>
      <tr><td class="spirala"><img class="spirala" src="img/spirala_czerwona.png" alt="" /></td><td>praca grzałki</td></tr>
      <tr><td class="cyrkulacja"><img class="cyrkulacja" src="img/cyrkulacja_szara.png" alt="" /></td><td>opcja cyrkulacji wyłączona</td></tr>
      <tr><td class="cyrkulacja"><img class="cyrkulacja" src="img/cyrkulacja_czarna.png" alt="" /></td><td>opcja cyrkulacji włączona</td></tr>
      <tr><td class="cyrkulacja"><img class="cyrkulacja" src="img/cyrkulacja_czerwona.png" alt="" /></td><td>praca cyrkulacji CWU</td></tr>
      <tr><td class="cyrkulacja"><img class="cyrkulacja" src="img/manual.png" alt="" /></td><td>tryb ręczny</td></tr>
      </table>
    </div>
  </div>
  
</div>
