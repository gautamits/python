from itertools import groupby
def ret(i):
	count=i
	total=count
	while count>0:
		total=total+(count-1)
		count-=1
	#print total
	return total
	
for _ in xrange(int(raw_input())):
	raw_input()
	arr=map(int,raw_input().split())
	res=[]
	for i,j in groupby(arr):
		res.append(len(list(j)))
	#print res
	sum=0
	for i in res:
		sum=sum+ret(i)
	print sum
		
