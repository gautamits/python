for _ in xrange(int(raw_input())):
	k=int(raw_input())
	a=raw_input()
	b=raw_input()
	c=raw_input()
	a=int(a,16)
	b=int(b,16)
	c=int(c,16)
	a=bin(a)[2:]
	b=bin(b)[2:]
	c=bin(c)[2:]
	m=len(a)
	n=len(b)
	o=len(c)
	l=max(m,n,o)
	print (l-m)*"0"+a
	print (l-n)*"0"+b
	print (l-o)*"0"+c
