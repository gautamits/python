from math import ceil
for _ in xrange(int(raw_input())):
	a,b=raw_input().split()
	if a%b != 0:
		print int(b)*ceil(float(a)/int(b))
	else :
		print int(b)*((int(a)/int(b))+1)