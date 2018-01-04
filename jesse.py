m,n=map(int,raw_input().split())
from itertools import groupby
arr=map(int,raw_input().split())
f=[len(list(group)) for key,group in groupby(sorted(arr))]
a=list(set(arr))
b=[i for i in xrange(1,len(arr)+1)]
c=sorted(zip(arr,b))
m={}
for i,j in c:
	m[j]=i
print m
print c
a=[i for i,j in c]
print a
print f
for _ in xrange(n):
	res=[]
	d=int(raw_input())
	for i in a:
		if i+d in a:
			res.append((a.index(i),a.index(i+d)))
			continue
	print res


