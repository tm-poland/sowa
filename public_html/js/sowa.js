
function StatusTask() {
    setTimeout(function () {
        PobierzStatus();
        StatusTask();
    }, 10000);
}


function SendConfig() {
   
  var selectBox = document.konfiguracja.opcja;
  var wartosc = document.konfiguracja.wartosc.value;
  var pass = document.konfiguracja.pass.value;  
  var option = selectBox.options[selectBox.selectedIndex];
	var optgroup = option.parentNode;
  
  if (pass != "")
  {
    if ((option.text != "") && (wartosc != ""))
    {

      if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
      } else { // code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
      xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {

          if (xmlhttp.responseText == "OK.")
          {
            document.konfiguracja.wartosc.className="ok";
            document.konfiguracja.pass.className="ok";
          }
          else if (xmlhttp.responseText == "BADPASSWORD.")
          {
            document.konfiguracja.pass.className="error";
          }
          else 
          {
            document.konfiguracja.wartosc.className="error";
            document.konfiguracja.pass.className="ok";
          }
        }
      }
      xmlhttp.open("POST","client-server.php?type=config",true);
      
      
      
      params = "message=CONFIG\n" + md5(pass) + "\n:"+optgroup.label+"."+option.text+"="+wartosc+"\n:END.";
      //alert(params);
      xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
      xmlhttp.setRequestHeader("Content-length", params.length);
      xmlhttp.setRequestHeader("Connection", "close");
    
      xmlhttp.send(params);
    } else {
      document.konfiguracja.wartosc.className="pusty";
    }
  } else {
      document.konfiguracja.pass.className="error";
  }
}

function GetConfig(selectBox) {

  document.konfiguracja.wartosc.className="pusty";
  
  var option = selectBox.options[selectBox.selectedIndex];
	var optgroup = option.parentNode;
  
  if (option.text != "")
  {
  
    if (window.XMLHttpRequest) {
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else { // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {

        document.konfiguracja.wartosc.value = xmlhttp.responseText;
        if (xmlhttp.responseText.toLowerCase() == "true") { 
          document.konfiguracja.TakNie1[0].checked = true;
        } else if (xmlhttp.responseText.toLowerCase() == "false") {
          document.konfiguracja.TakNie1[1].checked = true;
        } else {
          document.konfiguracja.TakNie1[0].checked = false;
          document.konfiguracja.TakNie1[1].checked = false;
        }
      }
    }
    xmlhttp.open("POST","client-server.php",true);
    
    params = "message=GETCONFIG:"+optgroup.label+":"+option.text+":END.";
    
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("Content-length", params.length);
    xmlhttp.setRequestHeader("Connection", "close");
  
    xmlhttp.send(params);
  } else {
    document.konfiguracja.wartosc.value = "";
  }

}

function TakNie(radio)
{
  if (radio.checked)
  {
    if (radio.value == "True") {
      document.konfiguracja.wartosc.value = "True";
    } else {
      document.konfiguracja.wartosc.value = "False";
    }
  } 
}

function Zmiana(obj)
{
  obj.className="pusty";
}

function SprawdzDaty(obj)
{
  
  if (obj.od_dzien.value == "" || obj.od_dzien.value > 31 || obj.od_dzien.value < 0) {                                                   
    obj.od_dzien.className = "error";
    return false;
  }
  
  if (obj.od_miesiac.value == "") {
    obj.od_miesiac.className = "error";
    return false;
  }
  
  if (obj.od_rok.value == "" || obj.od_rok.value > 9999 || obj.od_rok.value < 0) {
    obj.od_rok.className = "error";
    return false;
  }
  
  if (obj.od_godzina.value == "" || obj.od_godzina.value > 23 || obj.od_godzina.value < 0) {
    obj.od_godzina.className = "error";
    return false;
  }
  
  if (obj.od_minuta.value == "" || obj.od_minuta.value > 59 || obj.od_minuta.value < 0) {
    obj.od_minuta.className = "error";
    return false;
  }
  
  if (obj.do_dzien.value == "" || obj.do_dzien.value > 31 || obj.do_dzien.value < 0) {
    obj.do_dzien.className = "error";
    return false;
  }
  
  if (obj.do_miesiac.value == "") {
    obj.do_miesiac.className = "error";
    return false;
  }
  
  if (obj.do_rok.value == "" || obj.do_rok.value > 9999 || obj.do_rok.value < 0) {
    obj.do_rok.className = "error";
    return false;
  }
  
  if (obj.do_godzina.value == "" || obj.do_godzina.value > 23 || obj.do_godzina.value < 0) {
    obj.do_godzina.className = "error";
    return false;
  }
  
  if (obj.do_minuta.value == "" || obj.do_minuta.value > 59 || obj.do_minuta.value < 0) {
    obj.do_minuta.className = "error";
    return false;
  }
                                             
  obj.od_dzien.className = "pusty";
  obj.od_rok.className = "pusty";
  obj.od_godzina.className = "pusty";
  obj.od_minuta.className = "pusty";
  obj.do_dzien.className = "pusty";
  obj.do_rok.className = "pusty";
  obj.do_godzina.className = "pusty";
  obj.do_minuta.className = "pusty";
  
  return true;
}


function GetHistoria(startod) {

  var obj = document.historia;
  
  if (SprawdzDaty(obj) != true) return;

  document.getElementById("cont_historia").style.display = "block";
  document.getElementById("cont_historia").innerHTML = "<img src='img/loading.gif' />";
  
  if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else { // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      //document.getElementById("txtHint").innerHTML="<pre>"+xmlhttp.responseText+"</pre>";
      document.getElementById("cont_historia").innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("POST","client-historia.php",true);
  
  params = "od_dzien="+obj.od_dzien.value
    +"&"+"od_miesiac="+obj.od_miesiac.value
    +"&"+"od_rok="+obj.od_rok.value
    +"&"+"od_godzina="+obj.od_godzina.value
    +"&"+"od_minuta="+obj.od_minuta.value
    +"&"+"do_dzien="+obj.do_dzien.value  
    +"&"+"do_miesiac="+obj.do_miesiac.value
    +"&"+"do_rok="+obj.do_rok.value
    +"&"+"do_godzina="+obj.do_godzina.value
    +"&"+"do_minuta="+obj.do_minuta.value
    +"&"+"wynikow="+obj.wynikow.value
    +"&"+"start="+startod
    +"&"+"baza="+obj.baza.value;
  
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.setRequestHeader("Content-length", params.length);
  xmlhttp.setRequestHeader("Connection", "close");

  xmlhttp.send(params);

}

function GetDates(form, cont) {

  if (form.baza.value == "") return;

  document.getElementById(cont).style.display = "block";
  document.getElementById(cont).innerHTML = "<img src='img/loading.gif' />";
  
  if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else { // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      
      var tab = xmlhttp.responseText.split(';');
      if (tab.length < 10) {
        document.getElementById(cont).innerHTML = "Odpowiedź ma niepoprawny format: <pre>"
          + xmlhttp.responseText + "</pre>" ;
          return false;
      }
      
      form.od_dzien.value = tab[0];
      form.od_miesiac.value = parseInt(tab[1]);
      form.od_rok.value = tab[2];
      form.od_godzina.value = tab[3];
      form.od_minuta.value = tab[4];
      
      form.do_dzien.value = tab[5];
      form.do_miesiac.value = parseInt(tab[6]);
      form.do_rok.value = tab[7];
      form.do_godzina.value = tab[8];
      form.do_minuta.value = tab[9];
      
      document.getElementById(cont).innerHTML = "";
      document.getElementById(cont).style.display = "none";
    }
  }
  
  xmlhttp.open("POST","client-db-dates.php",true);
  
  params = "baza="+form.baza.value;
  
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.setRequestHeader("Content-length", params.length);
  xmlhttp.setRequestHeader("Connection", "close");

  xmlhttp.send(params);
}

function GetStatystyki() {

  var obj = document.statystyki; 
  
  if (SprawdzDaty(obj) != true) return;

  document.getElementById("cont_statystyki").style.display = "block";
  document.getElementById("cont_statystyki").innerHTML = "<img src='img/loading.gif' />";
  
  if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else { // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      //document.getElementById("txtHint").innerHTML="<pre>"+xmlhttp.responseText+"</pre>";
      document.getElementById("cont_statystyki").innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("POST","client-statystyki.php",true);
  
  params = "od_dzien="+obj.od_dzien.value
    +"&"+"od_miesiac="+obj.od_miesiac.value
    +"&"+"od_rok="+obj.od_rok.value
    +"&"+"od_godzina="+obj.od_godzina.value
    +"&"+"od_minuta="+obj.od_minuta.value
    +"&"+"do_dzien="+obj.do_dzien.value  
    +"&"+"do_miesiac="+obj.do_miesiac.value
    +"&"+"do_rok="+obj.do_rok.value
    +"&"+"do_godzina="+obj.do_godzina.value
    +"&"+"do_minuta="+obj.do_minuta.value
    +"&"+"baza="+obj.baza.value;
  
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.setRequestHeader("Content-length", params.length);
  xmlhttp.setRequestHeader("Connection", "close");

  xmlhttp.send(params);

}

function GetNormalLog(lines, id) {
  
  var obj = document.dzienniki;

  if (obj.normal.checked)
  {
    if (lines == 0) document.getElementById("container_log_normal").style.display = "block";
    if (lines == 0) document.getElementById("cont_log_normal").innerHTML = "<img src='img/loading.gif' />";
    
    if (window.XMLHttpRequest) {
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else { // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {

        if (lines > 0) {
          if (xmlhttp.responseText.length > 0)
            document.getElementById("cont_log_normal").innerHTML = document.getElementById("cont_log_normal").innerHTML + xmlhttp.responseText;
        } else {
          //if (xmlhttp.responseText.length > 0)
          document.getElementById("cont_log_normal").innerHTML = xmlhttp.responseText;
        }
         
        if (document.dzienniki.obserwuj.checked)
          setTimeout(function () { GetNormalLog(1, id); }, 1000);
      }
    }
    xmlhttp.open("POST","client-log.php",false);

    params = "type="+"normal"
      +"&"+"offset="+obj.snormal.value
      +"&"+"lines="+lines
      +"&"+"id="+id;
    
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("Content-length", params.length);
    xmlhttp.setRequestHeader("Connection", "close");
  
    xmlhttp.send(params);
  }
}

function GetErrorLog(lines, id) {
  
  var obj = document.dzienniki;
  
  if (obj.error.checked)
  {
    if (lines == 0) document.getElementById("container_log_error").style.display = "block";
    if (lines == 0) document.getElementById("cont_log_error").innerHTML = "<img src='img/loading.gif' />";
    
    if (window.XMLHttpRequest) {
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp2=new XMLHttpRequest();
    } else { // code for IE6, IE5
      xmlhttp2=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp2.onreadystatechange=function() {
      if (xmlhttp2.readyState==4 && xmlhttp2.status==200) {
        
        if (lines > 0) {
          if (xmlhttp2.responseText.length > 0)
            document.getElementById("cont_log_error").innerHTML = document.getElementById("cont_log_error").innerHTML + xmlhttp2.responseText;
        } else {
          //if (xmlhttp2.responseText.length > 0)
          document.getElementById("cont_log_error").innerHTML = xmlhttp2.responseText; 
        }
        
        if (document.dzienniki.obserwuj.checked) {
          setTimeout(function () { GetErrorLog(1, id); }, 1000);
        }
      }
    }
    xmlhttp2.open("POST","client-log.php",false);

    params = "type="+"error"
      +"&"+"offset="+obj.serror.value
      +"&"+"lines="+lines
      +"&"+"id="+id;
    
    xmlhttp2.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp2.setRequestHeader("Content-length", params.length);
    xmlhttp2.setRequestHeader("Connection", "close");
  
    xmlhttp2.send(params);
  }
}

function GetLogs() {
  document.getElementById("container_log_normal").style.display = "none";
  document.getElementById("cont_log_normal").innerHTML = "";
  document.getElementById("container_log_error").style.display = "none";
  document.getElementById("cont_log_error").innerHTML = "";
  GetNormalLog(0, randomString(5));
  GetErrorLog(0, randomString(5));
}

function randomString(string_length) {
	var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
	var randomstring = '';
	for (var i=0; i<string_length; i++) {
		var rnum = Math.floor(Math.random() * chars.length);
		randomstring += chars.substring(rnum,rnum+1);
	}
	return randomstring;
}

function utf8_encode(argString) {
  //  discuss at: http://phpjs.org/functions/utf8_encode/
  // original by: Webtoolkit.info (http://www.webtoolkit.info/)
  // improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // improved by: sowberry
  // improved by: Jack
  // improved by: Yves Sucaet
  // improved by: kirilloid
  // bugfixed by: Onno Marsman
  // bugfixed by: Onno Marsman
  // bugfixed by: Ulrich
  // bugfixed by: Rafal Kukawski
  // bugfixed by: kirilloid
  //   example 1: utf8_encode('Kevin van Zonneveld');
  //   returns 1: 'Kevin van Zonneveld'

  if (argString === null || typeof argString === 'undefined') {
    return '';
  }

  // .replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  var string = (argString + '');
  var utftext = '',
    start, end, stringl = 0;

  start = end = 0;
  stringl = string.length;
  for (var n = 0; n < stringl; n++) {
    var c1 = string.charCodeAt(n);
    var enc = null;

    if (c1 < 128) {
      end++;
    } else if (c1 > 127 && c1 < 2048) {
      enc = String.fromCharCode(
        (c1 >> 6) | 192, (c1 & 63) | 128
      );
    } else if ((c1 & 0xF800) != 0xD800) {
      enc = String.fromCharCode(
        (c1 >> 12) | 224, ((c1 >> 6) & 63) | 128, (c1 & 63) | 128
      );
    } else {
      // surrogate pairs
      if ((c1 & 0xFC00) != 0xD800) {
        throw new RangeError('Unmatched trail surrogate at ' + n);
      }
      var c2 = string.charCodeAt(++n);
      if ((c2 & 0xFC00) != 0xDC00) {
        throw new RangeError('Unmatched lead surrogate at ' + (n - 1));
      }
      c1 = ((c1 & 0x3FF) << 10) + (c2 & 0x3FF) + 0x10000;
      enc = String.fromCharCode(
        (c1 >> 18) | 240, ((c1 >> 12) & 63) | 128, ((c1 >> 6) & 63) | 128, (c1 & 63) | 128
      );
    }
    if (enc !== null) {
      if (end > start) {
        utftext += string.slice(start, end);
      }
      utftext += enc;
      start = end = n + 1;
    }
  }

  if (end > start) {
    utftext += string.slice(start, stringl);
  }

  return utftext;
}

function md5(str) {
  //  discuss at: http://phpjs.org/functions/md5/
  // original by: Webtoolkit.info (http://www.webtoolkit.info/)
  // improved by: Michael White (http://getsprink.com)
  // improved by: Jack
  // improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  //    input by: Brett Zamir (http://brett-zamir.me)
  // bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  //  depends on: utf8_encode
  //   example 1: md5('Kevin van Zonneveld');
  //   returns 1: '6e658d4bfcb59cc13f96c14450ac40b9'

  var xl;

  var rotateLeft = function (lValue, iShiftBits) {
    return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits));
  };

  var addUnsigned = function (lX, lY) {
    var lX4, lY4, lX8, lY8, lResult;
    lX8 = (lX & 0x80000000);
    lY8 = (lY & 0x80000000);
    lX4 = (lX & 0x40000000);
    lY4 = (lY & 0x40000000);
    lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
    if (lX4 & lY4) {
      return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
    }
    if (lX4 | lY4) {
      if (lResult & 0x40000000) {
        return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
      } else {
        return (lResult ^ 0x40000000 ^ lX8 ^ lY8);
      }
    } else {
      return (lResult ^ lX8 ^ lY8);
    }
  };

  var _F = function (x, y, z) {
    return (x & y) | ((~x) & z);
  };
  var _G = function (x, y, z) {
    return (x & z) | (y & (~z));
  };
  var _H = function (x, y, z) {
    return (x ^ y ^ z);
  };
  var _I = function (x, y, z) {
    return (y ^ (x | (~z)));
  };

  var _FF = function (a, b, c, d, x, s, ac) {
    a = addUnsigned(a, addUnsigned(addUnsigned(_F(b, c, d), x), ac));
    return addUnsigned(rotateLeft(a, s), b);
  };

  var _GG = function (a, b, c, d, x, s, ac) {
    a = addUnsigned(a, addUnsigned(addUnsigned(_G(b, c, d), x), ac));
    return addUnsigned(rotateLeft(a, s), b);
  };

  var _HH = function (a, b, c, d, x, s, ac) {
    a = addUnsigned(a, addUnsigned(addUnsigned(_H(b, c, d), x), ac));
    return addUnsigned(rotateLeft(a, s), b);
  };

  var _II = function (a, b, c, d, x, s, ac) {
    a = addUnsigned(a, addUnsigned(addUnsigned(_I(b, c, d), x), ac));
    return addUnsigned(rotateLeft(a, s), b);
  };

  var convertToWordArray = function (str) {
    var lWordCount;
    var lMessageLength = str.length;
    var lNumberOfWords_temp1 = lMessageLength + 8;
    var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
    var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
    var lWordArray = new Array(lNumberOfWords - 1);
    var lBytePosition = 0;
    var lByteCount = 0;
    while (lByteCount < lMessageLength) {
      lWordCount = (lByteCount - (lByteCount % 4)) / 4;
      lBytePosition = (lByteCount % 4) * 8;
      lWordArray[lWordCount] = (lWordArray[lWordCount] | (str.charCodeAt(lByteCount) << lBytePosition));
      lByteCount++;
    }
    lWordCount = (lByteCount - (lByteCount % 4)) / 4;
    lBytePosition = (lByteCount % 4) * 8;
    lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition);
    lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
    lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
    return lWordArray;
  };

  var wordToHex = function (lValue) {
    var wordToHexValue = '',
      wordToHexValue_temp = '',
      lByte, lCount;
    for (lCount = 0; lCount <= 3; lCount++) {
      lByte = (lValue >>> (lCount * 8)) & 255;
      wordToHexValue_temp = '0' + lByte.toString(16);
      wordToHexValue = wordToHexValue + wordToHexValue_temp.substr(wordToHexValue_temp.length - 2, 2);
    }
    return wordToHexValue;
  };

  var x = [],
    k, AA, BB, CC, DD, a, b, c, d, S11 = 7,
    S12 = 12,
    S13 = 17,
    S14 = 22,
    S21 = 5,
    S22 = 9,
    S23 = 14,
    S24 = 20,
    S31 = 4,
    S32 = 11,
    S33 = 16,
    S34 = 23,
    S41 = 6,
    S42 = 10,
    S43 = 15,
    S44 = 21;

  str = this.utf8_encode(str);
  x = convertToWordArray(str);
  a = 0x67452301;
  b = 0xEFCDAB89;
  c = 0x98BADCFE;
  d = 0x10325476;

  xl = x.length;
  for (k = 0; k < xl; k += 16) {
    AA = a;
    BB = b;
    CC = c;
    DD = d;
    a = _FF(a, b, c, d, x[k + 0], S11, 0xD76AA478);
    d = _FF(d, a, b, c, x[k + 1], S12, 0xE8C7B756);
    c = _FF(c, d, a, b, x[k + 2], S13, 0x242070DB);
    b = _FF(b, c, d, a, x[k + 3], S14, 0xC1BDCEEE);
    a = _FF(a, b, c, d, x[k + 4], S11, 0xF57C0FAF);
    d = _FF(d, a, b, c, x[k + 5], S12, 0x4787C62A);
    c = _FF(c, d, a, b, x[k + 6], S13, 0xA8304613);
    b = _FF(b, c, d, a, x[k + 7], S14, 0xFD469501);
    a = _FF(a, b, c, d, x[k + 8], S11, 0x698098D8);
    d = _FF(d, a, b, c, x[k + 9], S12, 0x8B44F7AF);
    c = _FF(c, d, a, b, x[k + 10], S13, 0xFFFF5BB1);
    b = _FF(b, c, d, a, x[k + 11], S14, 0x895CD7BE);
    a = _FF(a, b, c, d, x[k + 12], S11, 0x6B901122);
    d = _FF(d, a, b, c, x[k + 13], S12, 0xFD987193);
    c = _FF(c, d, a, b, x[k + 14], S13, 0xA679438E);
    b = _FF(b, c, d, a, x[k + 15], S14, 0x49B40821);
    a = _GG(a, b, c, d, x[k + 1], S21, 0xF61E2562);
    d = _GG(d, a, b, c, x[k + 6], S22, 0xC040B340);
    c = _GG(c, d, a, b, x[k + 11], S23, 0x265E5A51);
    b = _GG(b, c, d, a, x[k + 0], S24, 0xE9B6C7AA);
    a = _GG(a, b, c, d, x[k + 5], S21, 0xD62F105D);
    d = _GG(d, a, b, c, x[k + 10], S22, 0x2441453);
    c = _GG(c, d, a, b, x[k + 15], S23, 0xD8A1E681);
    b = _GG(b, c, d, a, x[k + 4], S24, 0xE7D3FBC8);
    a = _GG(a, b, c, d, x[k + 9], S21, 0x21E1CDE6);
    d = _GG(d, a, b, c, x[k + 14], S22, 0xC33707D6);
    c = _GG(c, d, a, b, x[k + 3], S23, 0xF4D50D87);
    b = _GG(b, c, d, a, x[k + 8], S24, 0x455A14ED);
    a = _GG(a, b, c, d, x[k + 13], S21, 0xA9E3E905);
    d = _GG(d, a, b, c, x[k + 2], S22, 0xFCEFA3F8);
    c = _GG(c, d, a, b, x[k + 7], S23, 0x676F02D9);
    b = _GG(b, c, d, a, x[k + 12], S24, 0x8D2A4C8A);
    a = _HH(a, b, c, d, x[k + 5], S31, 0xFFFA3942);
    d = _HH(d, a, b, c, x[k + 8], S32, 0x8771F681);
    c = _HH(c, d, a, b, x[k + 11], S33, 0x6D9D6122);
    b = _HH(b, c, d, a, x[k + 14], S34, 0xFDE5380C);
    a = _HH(a, b, c, d, x[k + 1], S31, 0xA4BEEA44);
    d = _HH(d, a, b, c, x[k + 4], S32, 0x4BDECFA9);
    c = _HH(c, d, a, b, x[k + 7], S33, 0xF6BB4B60);
    b = _HH(b, c, d, a, x[k + 10], S34, 0xBEBFBC70);
    a = _HH(a, b, c, d, x[k + 13], S31, 0x289B7EC6);
    d = _HH(d, a, b, c, x[k + 0], S32, 0xEAA127FA);
    c = _HH(c, d, a, b, x[k + 3], S33, 0xD4EF3085);
    b = _HH(b, c, d, a, x[k + 6], S34, 0x4881D05);
    a = _HH(a, b, c, d, x[k + 9], S31, 0xD9D4D039);
    d = _HH(d, a, b, c, x[k + 12], S32, 0xE6DB99E5);
    c = _HH(c, d, a, b, x[k + 15], S33, 0x1FA27CF8);
    b = _HH(b, c, d, a, x[k + 2], S34, 0xC4AC5665);
    a = _II(a, b, c, d, x[k + 0], S41, 0xF4292244);
    d = _II(d, a, b, c, x[k + 7], S42, 0x432AFF97);
    c = _II(c, d, a, b, x[k + 14], S43, 0xAB9423A7);
    b = _II(b, c, d, a, x[k + 5], S44, 0xFC93A039);
    a = _II(a, b, c, d, x[k + 12], S41, 0x655B59C3);
    d = _II(d, a, b, c, x[k + 3], S42, 0x8F0CCC92);
    c = _II(c, d, a, b, x[k + 10], S43, 0xFFEFF47D);
    b = _II(b, c, d, a, x[k + 1], S44, 0x85845DD1);
    a = _II(a, b, c, d, x[k + 8], S41, 0x6FA87E4F);
    d = _II(d, a, b, c, x[k + 15], S42, 0xFE2CE6E0);
    c = _II(c, d, a, b, x[k + 6], S43, 0xA3014314);
    b = _II(b, c, d, a, x[k + 13], S44, 0x4E0811A1);
    a = _II(a, b, c, d, x[k + 4], S41, 0xF7537E82);
    d = _II(d, a, b, c, x[k + 11], S42, 0xBD3AF235);
    c = _II(c, d, a, b, x[k + 2], S43, 0x2AD7D2BB);
    b = _II(b, c, d, a, x[k + 9], S44, 0xEB86D391);
    a = addUnsigned(a, AA);
    b = addUnsigned(b, BB);
    c = addUnsigned(c, CC);
    d = addUnsigned(d, DD);
  }

  var temp = wordToHex(a) + wordToHex(b) + wordToHex(c) + wordToHex(d);

  return temp.toLowerCase();
}


$(document).ready(function(){
  
  /* onLoad */
  var sowa = {};
  PobierzStatus();
  StatusTask();
  
  $("#cwu").on("taphold dblclick", "#grzalka-switch", function (event) {
    event.preventDefault();
    ManualSwitch("grzalka");
  });  
  
  $("#cwu").on("taphold dblclick", "#cyrkulacja-switch", function (event) {
    event.preventDefault();
    ManualSwitch("cyrkulacja");
  });
      
}); 


function ManualSwitch(device)
{  
  if (!$.isEmptyObject(sowa))
  {
    var pass = prompt("Wpisz hasło:");
    
    if (pass != null)
    {
      $.post("client-server.php",
      {
        type: "config",
        message: "CONFIG\n" + md5(pass) + "\n:"+device+".manual="+((sowa[device+"_manual"] == 1) ? "False" : "True")+"\n:END."
      },
      function(data){
        if (data == "OK.") alert ("Operacja zakończona pomyślnie.");
        else alert ("Wystąpił błąd: "+ data);
      });
    }
  } 
}

function Load_JSON_Data()
{
  if (!$.isEmptyObject(sowa))
  {
    $("#error").html("");
  
    $("#general_temp_wew").html(parseFloat(sowa.general_temp_wew).toFixed(1) + "&deg;C");
    $("#general_temp_zew").html(parseFloat(sowa.general_temp_zew).toFixed(1) + "&deg;C");
    
    if (sowa.general_praca) {
      if (sowa.general_temp > 30) {
        $("#error").html("<p>Temperatura wewnątrz obudowy systemu jest zbyt wysoka!</p>");
        $("#serwer").addClass="serwer-error";
        $("#general_temp").html(parseFloat(sowa.general_temp).toFixed(1) + "&deg;C");
      } else {
        $("#serwer").addClass("serwer-normal");
      }  
    } else {
      $("#serwer").className="off"; 
    }
        
    $("#co_temp_zasilania").html(parseFloat(sowa.co_temp_zasilania).toFixed(1) + "&deg;C");
    $("#co_temp_powrotu").html(parseFloat(sowa.co_temp_powrotu).toFixed(1) + "&deg;C");
    $("#co_temp_spalin").html(parseFloat(sowa.termopara_temp).toFixed(1) + "&deg;C");
    
    if (sowa.co_rozpalanie) {
      $("#co").addClass("rozpalanie");  
    } else if (sowa.co_wygaszanie) {
      $("#co").addClass("wygaszanie");  
    } else if (sowa.co_praca) {
      $("#co").addClass("praca"); 
    } else if (sowa.co_on) {
      $("#co").addClass("on"); 
    } else {
      $("#co").addClass("off"); 
    }
       
    $("#cwu_temp").html(parseFloat(sowa.cwu_temp).toFixed(1) + "&deg;C");
    $("#cyrkulacja_temp").html(parseFloat(sowa.cyrkulacja_temp).toFixed(1) + "&deg;C");
    
    if (sowa.cwu_praca) {
      $("#cwu").addClass("praca");  
    } else if (sowa.cwu_on) {
      $("#cwu").addClass("on");     
    } else {
      $("#cwu").addClass("off"); 
    }
    
    if (sowa.grzalka_praca) {
      $("#grzalka_praca").html("<img class='grzalka' id='grzalka-switch' src='img/spirala_czerwona"+((sowa.grzalka_manual) ? "_manual" : "")+".png' />");
    } else if (sowa.grzalka_on) {
      $("#grzalka_praca").html("<img class='grzalka' id='grzalka-switch' src='img/spirala_czarna"+((sowa.grzalka_manual) ? "_manual" : "")+".png' />");
    } else {
      $("#grzalka_praca").html("<img class='grzalka' id='grzalka-switch' src='img/spirala_szara"+((sowa.grzalka_manual) ? "_manual" : "")+".png' />");
    }
    
    
    if (sowa.cyrkulacja_praca) {
      $("#cyrkulacja_praca").html("<img class='cyrkulacja' id='cyrkulacja-switch' src='img/cyrkulacja_czerwona"+((sowa.cyrkulacja_manual) ? "_manual" : "")+".png' />");
    } else if (sowa.grzalka_on) {
      $("#cyrkulacja_praca").html("<img class='cyrkulacja' id='cyrkulacja-switch' src='img/cyrkulacja_czarna"+((sowa.cyrkulacja_manual) ? "_manual" : "")+".png' />");
    } else {
      $("#cyrkulacja_praca").html("<img class='cyrkulacja' id='cyrkulacja-switch' src='img/cyrkulacja_szara"+((sowa.cyrkulacja_manual) ? "_manual" : "")+".png' />");
    }
  
    $("#ogrzewanie_podlogowe_temp").html(parseFloat(sowa.ogrzewanie_podlogowe_temp).toFixed(1) + "&deg;C");
  
    if (sowa.ogrzewanie_podlogowe_praca) {
      $("#ogrzewanie_podlogowe").addClass("praca");  
    } else if (sowa.ogrzewanie_podlogowe_on) {
      $("#ogrzewanie_podlogowe").addClass("on"); 
    } else {
      $("#ogrzewanie_podlogowe").addClass("off"); 
    }
  } else {
    $("#co").addClass("off");
    $("#cwu").addClass("off");
    $("#grzalka_praca").html("<img class='grzalka' id='grzalka-switch' src='img/spirala_szara.png' />");
    $("#cyrkulacja_praca").html("<img class='cyrkulacja' id='cyrkulacja-switch' src='img/cyrkulacja_szara.png' />");
    $("#ogrzewanie_podlogowe").addClass("off");
    //document.getElementById("serwer").addClass="off";
    $("#error").html("<p>Błąd połączenia z serwerem!</p>");
    $("#serwer").addClass("serwer-error");
  }
}

function PobierzStatus() {
  $.post("client-server.php",
  {
    message: "STATUS"
  },
  function(data){
    sowa = $.parseJSON(data);
    if (location.search == "") Load_JSON_Data(data);
  });
}