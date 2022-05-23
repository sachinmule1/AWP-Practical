#!"C:/xampp/perl/bin/perl.exe"
use CGI ':standard';
use DBI;
print "Content-type:text/html\n\n";
$name=param('name');
$age=param('age');
$dbh=DBI->connect('DBI:mysql:test',"root","")
or die "error connect:DBI->errstr()";
$qh=$dbh->prepare("insert into user values('$name','$age')")
or die "can't execute query:$dbh->errstr()";
$qh->execute();
$qh=$dbh->prepare("Select * from user");
$qh->execute();

print "<table border size=1><tr><th>Name</th><th>Age</th></tr>";
while (($name,$age)=$qh->fetchrow())
{
print "<tr><td>$name</td><td>$age</td></tr>";
}
print "</table>";
$qh->finish();
$dbh->disconnect();
print end_html();

