#!"c:/Xampp/perl/bin/perl.exe"
#Write a CGI-Perl program to use a cookie to remember the day of the last login
#from a user and display it when run.
use CGI ":standard";
@last_day = cookie('last_time');
$day_of_week = (qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday)) 
[(localtime)[6]];
$month = (qw(January February March April May June July August September October November December))
[(localtime)[4]];
$day_of_month = (localtime)[3];
@day_stuff = ($day_of_week, $day_of_month, $month); 
$day_cookie = cookie(-name => 'last_time',-value => \@day_stuff,-expires => '+5d');
print header(-cookie => $day_cookie);
print start_html('This is day_cookie.pl');
if (scalar(@last_day) == 0) {
    print "Welcome to you on your first visit to our site <br />";
}
else {
    ($day_of_week, $day_of_month, $month) = @last_day;
    print "Welcome back! <br /> ",
          "Your last visit was on ",
          "$day_of_week, $month $day_of_month <br />";
}
print end_html;
