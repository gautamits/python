num=raw_input()
for _ in xrange(int(raw_input())):
	l,r=map(int,raw_input().split())
	number=int(num[l-1:r])
	result="NO"
	while True:
		if number >= 7 and number <= 70:
			if number % 7==0:
				result="YES"
			else:
				result="NO"
			break
		else:
			i=number/10
			number=number-i*2
	print result
	#print number
	
