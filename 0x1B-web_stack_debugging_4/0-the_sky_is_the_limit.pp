# Fixing limited requests problem 
exec { "sed -i 's/15/2000/' /etc/default/nginx && sudo service nginx restart":
path => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
