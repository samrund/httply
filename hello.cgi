#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new

if cgi['user'] == ''
  honorriffics = ['Mr. President', 'Your. Highness', 'Dear Leader']
  greeting = honorriffics.sample
else
  greeting = cgi['user']
end

puts cgi.header

<!doctype html>
<html>
  <head>
    <title> Mind . . . Blown </title>
  </head>

  <body>
    Hello, #{greeting}.
  </body>
</html>"
