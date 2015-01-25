<?php

class MyDB extends SQLite3
{
  public $db_name;
    
  function __construct($param)
  {
      $this->db_name = $param;
      $this->open($this->db_name);
  }
}

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

?>
