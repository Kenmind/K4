# installs and configures Nginx web server
exec {'apt-get update':
  path => '/usr/bin'
}
package {'nginx':
}
file {'index.html':
  ensure  => 'present',
  path    => '/etc/nginx/html/index.html',
  content => 'Hello World!',
}
file {'404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
  path    => '/etc/nginx/html/404.html',
}
file {'default':
  ensure  => 'present',
  path    => '/etc/nginx/html/default',
  content => "server {\n\tlisten 80;\n\tlisten [::]:80 default_server;\n\troot   /etc/nginx/html;\n\tindex  index.html index.htm;\n\tlocation /redirect_me {\n\t\treturn 301 http://youtube.com/UCw4X_zayaSiuVYcqWpiaSWw;\n\t}\n\terror_page 404 /404.html;\n\tlocation /404 {\n\t\troot /etc/nginx/html;\n\t\tinternal;\n\t }\n}"
}
