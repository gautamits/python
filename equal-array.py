from sets import Set
import math
def prime(i):
	j=2
	flag=False
	result=[]
	while j < i:
		if i % j == 0:
			result.append(j)
			flag=True
		j+=1
	if flag==False:
		result.append(i)
	return result

def needy(arr):
	res=[]
	for i in arr:
		res.append(prime(i))
	#print res
	return res
	
	
	
for _ in xrange(int(raw_input())):
	n,x,y,z=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	need=needy(arr)
	#print need
	not_needed=Set(need[0])
	needed=Set(need[0])
	for i in need:
		not_needed=not_needed.intersection(Set(i))
		needed=needed.union(Set(i))
	needed=needed.difference(not_needed)
	#print needed
	if needed.issubset(Set([x,y,z])):
		print "She can"
	else:
		print "She can't"
	
