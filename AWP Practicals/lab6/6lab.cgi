#!"C:/xampp/perl/bin/perl.exe"

print "refresh:1 \n";
print "content-type:text/html \n\n";

use CGI':standard';
($s,$m,$h)=localtime(time);

print "$h:$m:$s";
print "<br><br>$h Hours $m Minutes $s Seconds";