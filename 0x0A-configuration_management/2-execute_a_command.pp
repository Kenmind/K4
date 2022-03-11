# Kills a process named killmenow
#	syscall: exec
#	command: pkill

exec {'pkill -f killmenow':
path => '/usr/bin/:usr/local/bin/:/bin/'
}
