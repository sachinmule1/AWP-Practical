#!"C:/Xampp/perl/bin/perl.exe"
#Write a Perl program to display a digital clock which displays the 
#current time of the server.
print "refresh:1 \n";
print "content-type:text/html \n\n";

use CGI':standard';
($s,$m,$h)=localtime(time);
print "$h:$m:$s";
print "<br/><br/>$h hours $m minutes $s seconds";
