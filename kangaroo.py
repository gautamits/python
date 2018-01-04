	
a,d1,b,d2=raw_input().split()
a=int(a)
b=int(b)
d1=int(d1)
d2=int(d2)
if a<b and d1 < d2:
	print 'NO'
	exit(0)
n=float(a-b)/(d2-d1)
if n==int(n):
	print 'YES'
else:
	print 'NO'
