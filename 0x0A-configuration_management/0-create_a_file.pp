# creates a file in /tmp with:
#	name: school
#	permission: 0744
#	owner: www-data
#	group: www-data
#	content: I love Puppet

file {'school':
ensure  => 'present',
path    => '/tmp/school',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet',
}
