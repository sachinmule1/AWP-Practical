#!"C:\xampp\perl\bin\perl.exe"
use CGI':standard';
@msgs=("Welcome " ,"have a nice day","hi","how are you");
$len=@msgs.length;
$n = int(rand($len));
if (param)
{
print header( );
 print start_html();
$name=param("name");
print b("Hello $name $msgs[$n]"),br();
print start_form();
print submit(-value=>"Back");
print end_form();
print end_html();
}
else
{
print header();
print start_html(-text =>"blue");
print start_form();
print b("Enter user name ");
print textfield(-name=>"name"),br();
print submit(-value =>"submit");
print end_form();
print end_html();
}