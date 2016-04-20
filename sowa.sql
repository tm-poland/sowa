-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Czas wygenerowania: 02 Sty 2015, 09:49
-- Wersja serwera: 5.5.40
-- Wersja PHP: 5.4.35-0+deb7u2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Baza danych: `sowa`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `historia`
--

CREATE TABLE IF NOT EXISTS `historia` (
  `czas` int(10) unsigned NOT NULL,
  `trwanie` int(10) unsigned NOT NULL,
  `co_praca` tinyint(1) unsigned NOT NULL,
  `co_rozpalanie` tinyint(1) unsigned NOT NULL,
  `co_wygaszanie` tinyint(1) unsigned NOT NULL,
  `co_temp_zasilania` float(5,2) NOT NULL,
  `co_temp_powrotu` float(5,2) NOT NULL,
  `cwu_praca` tinyint(1) unsigned NOT NULL,
  `cwu_temp` float(5,2) NOT NULL,
  `ogrzewanie_podlogowe_praca` tinyint(1) unsigned NOT NULL,
  `ogrzewanie_podlogowe_temp` float(5,2) NOT NULL,
  `cyrkulacja_praca` tinyint(1) unsigned NOT NULL,
  `cyrkulacja_temp` float(5,2) NOT NULL,
  `grzalka_praca` tinyint(1) unsigned NOT NULL,
  `temp` float(5,2) NOT NULL,
  `temp_wew` float(5,2) NOT NULL,
  `temp_zew` float(5,2) NOT NULL,
  `termopara_temp` float(6,2) NOT NULL,
  PRIMARY KEY (`czas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- Zmiana 20151105
ALTER TABLE `historia` CHANGE `co_temp_zasilania` `co_temp_zasilania` FLOAT( 5, 2 ) NULL ,
CHANGE `co_temp_powrotu` `co_temp_powrotu` FLOAT( 5, 2 ) NULL ,
CHANGE `cwu_temp` `cwu_temp` FLOAT( 5, 2 ) NULL ,
CHANGE `ogrzewanie_podlogowe_temp` `ogrzewanie_podlogowe_temp` FLOAT( 5, 2 ) NULL ,
CHANGE `cyrkulacja_temp` `cyrkulacja_temp` FLOAT( 5, 2 ) NULL ,
CHANGE `temp` `temp` FLOAT( 5, 2 ) NULL ,
CHANGE `temp_wew` `temp_wew` FLOAT( 5, 2 ) NULL ,
CHANGE `temp_zew` `temp_zew` FLOAT( 5, 2 ) NULL ,
CHANGE `termopara_temp` `termopara_temp` FLOAT( 6, 2 ) NULL;