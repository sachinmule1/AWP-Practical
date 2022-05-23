#!"c:/Xampp/perl/bin/perl.exe"
#Write a Perl program to keep track of the number of visitors visiting the web page
#and to display this count of visitors, with proper headings.

use CGI ':standard';
print header(),
start_html(),
h1("DSCASC,MCA"),
hr();
$fname='count.txt';
if(open(FH,"<$fname"))
{
$c=<FH>;
$c=$c+1;
close(FH);
}
open(FH,">$fname");
print FH $c;
close(FH);
print "YOU ARE THE $c VISITOR";
print end_html();