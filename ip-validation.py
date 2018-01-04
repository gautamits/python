# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in xrange(int(raw_input())):
    s=raw_input()
    if len(re.findall(r'^[[0-9]{1,2}[0-5].]{3}[0-9]{1,2}[0-5]$',s)) == 1:
        print "IPv4"
    elif len(re.findall(r'^[[0-9abcdef]{4}}:]{7}[0-9abcdef]{4}$',s)) == 1:
        print "IPv6"
    else:
        print "Neither"
