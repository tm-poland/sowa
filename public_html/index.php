<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>SOWA1</title>
<script type="text/javascript" src="sowa.js"></script>
<link rel="stylesheet" href="sowa.css" />
</head>
<body <?php if (empty($_GET['site'])) { ?>onload="PobierzStatus();timeout();"<?php } ?>>

<div id="header">
  <h1>SOWA</h1>
</div>

<div id="nav">
  <ul>
    <?php if (empty($_GET['site'])) { ?>
    <li><a href="?site=historia">Historia</a></li>
    <li><a href="?site=statystyki">Statystyki</a></li>
    <li><a href="?site=konfiguracja">Konfiguracja</a></li>
    <li><a href="?site=dzienniki">Dzienniki</a></li>
    <?php } elseif ($_GET['site'] == 'konfiguracja') { ?>
    <li><a href="index.php">Stan</a></li>
    <li><a href="?site=historia">Historia</a></li>
    <li><a href="?site=statystyki">Statystyki</a></li>
    <li><a href="?site=dzienniki">Dzienniki</a></li>
    <?php } elseif ($_GET['site'] == 'historia') { ?>
    <li><a href="index.php">Stan</a></li>
    <li><a href="?site=statystyki">Statystyki</a></li>
    <li><a href="?site=konfiguracja">Konfiguracja</a></li>
    <li><a href="?site=dzienniki">Dzienniki</a></li>
    <?php } elseif ($_GET['site'] == 'statystyki') { ?>
    <li><a href="index.php">Stan</a></li>
    <li><a href="?site=historia">Historia</a></li>
    <li><a href="?site=konfiguracja">Konfiguracja</a></li>
    <li><a href="?site=dzienniki">Dzienniki</a></li>
    <?php } elseif ($_GET['site'] == 'dzienniki') { ?>
    <li><a href="index.php">Stan</a></li>
    <li><a href="?site=historia">Historia</a></li>
    <li><a href="?site=statystyki">Statystyki</a></li>
    <li><a href="?site=konfiguracja">Konfiguracja</a></li>
    <?php } ?>
  </ul>
</div>

<?php

if (empty($_GET['site'])) {
  require('stan.inc.php');
  
} elseif ($_GET['site'] == 'konfiguracja') {
  require('konfiguracja.inc.php');
  
} elseif ($_GET['site'] == 'historia') {
  require('historia.inc.php');
  
  } elseif ($_GET['site'] == 'statystyki') {
  require('statystyki.inc.php');
  
  } elseif ($_GET['site'] == 'dzienniki') {
  require('log.inc.php');
  
}


?>

<div id="footer">
  <p>&copy; 2014-2015 TM. Wszelkie prawa zastrzeżone.</p>
</div>

</body>
</html>
