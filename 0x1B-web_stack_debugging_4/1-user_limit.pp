# Fixing user limit
exec { 'Change ULIMIT':
￼  command  => 'echo -e "holberton hard nofile 2500\nholberton soft nofile 25000" > /etc/security/limits.conf',
   provider => shell,
}
