# SOWA
Przedmiotem projektu jest multisterownik/ multikontroler kotłowni wykorzystujący jako jednostkę centralną minikomputer Raspberry Pi B+

## Instalacja
Jestem w trakcie przygotowywania repozytorium. Jak będzie gotowe do użycia to zamieszczę tu informacje jak dokonać instalacji.

### Przygotowanie systemu
Na końcu pliku */etc/modules* dopisać dwie linie:
```
w1-gpio
w1-therm
```
### Serwer WWW
Serwer WWW nie jest potrzebny do działania serwera kotłowni jednak umożliwia skorzystanie z frontendu do odczytu stanów, korzystania ze statystyk, itp.

#### Instalacja serwera lighttp
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
``
Uruchamiamy ponownie serwer lighttpd:
`sudo service lighttpd restart`

Upewniamy się, że będzie uruchamiany automatycznie:
`sudo chkconfig lighttpd on`

#### Instalacja systemu bazy danych
System bazy danych nie jest wymagany do pracy, jednak pozwala na gromadzenie danych z pracy serwera kotłowni. Do wyboru mamy obsługę MySQL lub SQLite3. Można zapisywać dane do jednej lub drugiej bazy lub do dwóch jednocześnie.

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
`sudo apt-get install sqlite3`

### Instalacja serwera SOWA
```
sudo apt-get install git
cd
git clone https://github.com/tm-poland/sowa.git 
```
W katalogu użytkownika *pi* został utworzony katalog serwera *sowa*.

cdn.

## Licencja
Do zastanowienia.
