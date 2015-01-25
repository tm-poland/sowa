# SOWA
Przedmiotem projektu jest multisterownik/ multikontroler kotłowni wykorzystujący jako jednostkę centralną minikomputer Raspberry Pi B+

Opis działania, funkcje, zdjęcia można znaleźć tu: [Multisterownik/ multikontroler kotłowni na Raspberry Pi B+](http://www.elektroda.pl/rtvforum/topic2962538.html)

## Instalacja
### Uwaga!
Serwer napisałem pod swoją kotłownię. Jeżeli chesz go wykorzystać u siebie pamiętaj, że cała odpowiedzialność za bezpieczeństwo leży po Twojej stronie. Jeżeli nie do końca wiesz co robisz lepiej wykorzystaj dodatkowe zabezpieczenia. 

### Założenia
* Instalacja odbywa się na systemie Raspbian, korzystając z konta domyślnego użytkownika *pi*
* Katalog serwera umieszczony będzie w katalogu głównym użytkownika *pi*

### Przygotowanie systemu
Na końcu pliku */etc/modules* dopisać dwie linie:
```
w1-gpio
w1-therm
```

Instalujemy biblioteki dla Pythona:
```
sudo apt-get install python-mysqldb
```

### Serwer WWW
Serwer WWW nie jest potrzebny do działania serwera kotłowni jednak umożliwia skorzystanie z frontendu do odczytu stanów, korzystania ze statystyk, itp.

#### Instalacja serwera lighttpd
```
sudo apt-get install lighttpd php5-cgi
sudo lighttpd-enable-mod fastcgi
```
W pliku */etc/php5/cgi/php.ini* ustawiamy:
`cgi.fix_pathinfo=1`

Na końcu pliku */etc/lighttpd/lighttpd.conf* dopisujemy: 
```
fastcgi.server = ( ".php" => (("bin-path" => "/usr/bin/php5-cgi", "socket" => "/tmp/php.socket")))
alias.url += ( "/sowa" => "/home/pi/sowa/public_html/" )
```
Uruchamiamy ponownie serwer lighttpd:
`sudo service lighttpd restart`

Upewniamy się, że będzie uruchamiany automatycznie:
`sudo chkconfig lighttpd on`

#### Instalacja systemu bazy danych
System bazy danych nie jest wymagany do pracy, jednak pozwala na gromadzenie danych stanów serwera kotłowni. Do wyboru mamy obsługę MySQL lub SQLite3. Można zapisywać dane do jednej lub drugiej bazy lub do dwóch jednocześnie.

##### Instalacja MySQL
`apt-get install mysql-server mysql-client php5-mysql`

Upewniamy się, że serwer bazy będzie uruchamiany automatycznie:
`sudo chkconfig mysql on`

Tworzymy bazę danych o nazwie *sowa* na potrzeby projektu:
```
mysql -u root -p
CREATE DATABASE sowa;
quit;
```

##### Instalacja SQLite3
`sudo apt-get install sqlite3 php5-sqlite`

### Instalacja serwera SOWA
```
sudo apt-get install git
cd
git clone https://github.com/tm-poland/sowa.git 
```
1. W katalogu użytkownika *pi* został utworzony katalog serwera *sowa*.
2. Odnajdujemy w nim katalog *install* i kopiujemy w odpowiednie miejsca w sytemie pliki zawarte w tym katalogu zgodnie z jego ścieżką.
3. Ustawiamy odpowiednie własności:
```
sudo chown root:root /etc/init.d/sowa
sudo chown root:root /etc/logrotate.d/sowa
```
4. Ustawiamy automatyczny start/ stop serwera
`sudo update-rc.d sowa enable`

5. Teraz przyszedł czas na konfigurację pliku serwera SOWA */home/pi/sowa/sowa.conf* oraz frontendu */home/pi/sowa/public_html/config.inc.php*

6. Jeżeli wybraliśmy bazę danych SQLite3 należy ją zainicjować. Przechodzimy do katalogu, gdzie ma się znajdować (domyślnie w katalogu serwera, czyli */home/pi/sowa/*) i wpisujemy polecenia:
```
sqlite3 sowa.db
.exit
```
1. Możemy zrestartować RPi i brać się za dostosowywanie konfiguracji serwera SOWA do swoich potrzeb:
`sudo reboot`
2. Frontend jest dostępny pod adresem:
`http://ip_twojego_rpi/sowa`

## Licencja
Do użytku prywatnego - bez ograniczeń. W innych przypadkach proszę o [kontakt](https://github.com/tm-poland).
