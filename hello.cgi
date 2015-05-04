#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
puts cgi.header
page = 'home'
page = cgi['page'] unless cgi['page'].empty?

def render(page, &content)
  title = {
    'about'  => 'about us',
    'home'  => 'welcome'
  }
  puts"
    <!doctype html>
    <html>
      <head>
      <title> #{title[page]} </title>
      </head>
      <body>
        #{yield}
      </body>
    </html>"

end

render(page) do
  if page =='about'
    "We are coder."
  else
    "Welcome. Have a look around"
  end
end
