# Fixing limited requests problem 
exec { 'increasing_limits':
    command => 'sudo sed -i "s/15/3000/" /etc/default/nginx;
    	        sudo service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
