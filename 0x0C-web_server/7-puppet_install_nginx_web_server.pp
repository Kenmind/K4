# installs and configures Nginx web server

package {'nginx':
  ensure => 'installed',
}


file_line {'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'Listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://youtube.com/UCw4X_zayaSiuVYcqWpiaSWw permanent;',
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

service {'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
