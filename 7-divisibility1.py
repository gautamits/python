num=raw_input()
for _ in xrange(int(raw_input())):
	l,r=map(int,raw_input().split())
	number=num[l-1:r]
	#print number
	while len(number) > 2:
		print number
		first=number[0]
		number=number[1:]
		if 7 > int(first):
			first=first+number[0]
			number=number[1:]
		print "dividing ",first,"by 7"
		dividend=int(first)/7
		remainder=int(first)-dividend*7
		print dividend,remainder
		if remainder != 0:
			number=str(remainder)+number
	if int(number) %7 == 0:
		print "YES"
	else:
		print "NO"
