#!/usr/bin/env ruby
F = ARGV[0].scan(/from:(.*?)\]/)
t = ARGV[0].scan(/to:(.*?)\]/)
f = ARGV[0].scan(/flags:(.*?)\]/)
puts [F, t, f].join(',')
