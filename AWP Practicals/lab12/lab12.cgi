#!"C:\xampp\perl\bin\perl.exe"
use strict;
use CGI':standard';
print 
header(),
start_html(),
hr(),
h2("Server Information"),
hr(),
"Server Name : $ENV{SERVER_NAME}",
hr(),
"Server Protocol : $ENV{SERVER_SOFTWARE}",
hr(),
"Server Port : $ENV{SERVER_PORT}",
hr(),
"CGI Revision : $ENV{GATEWAY_INTERFACE}",
hr(),
"Script Name : $ENV{SCRIPT_NAME}",
hr(),
"Root Document : $ENV{DOCUMENT_ROOT}",
end_html();
