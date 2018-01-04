def dfs(n):
	res=[]
	while True:
		try:
			ind=parent[n].index(1)
			if ind==p:
				res.append(ind)
				break
			res.append(a[ind].index(1))
			n=a[ind].index(1)
			
		except:
			break
	return res

raw_input()
arr=map(int,raw_input().split())
s=[i for i in xrange(1,len(arr)+1)]
print s
a=[[0 for i in xrange(len(arr))] for j in xrange(len(arr))]
parent=[[0 for i in xrange(len(arr))] for j in xrange(len(arr))]
p=None
for i in xrange(1,len(arr)):
	x,y=map(int,raw_input().split())
	if p==None or p==y-1:
		p=x-1
	a[x-1][y-1]=1
	parent[y-1][x-1]=1
print a
print parent
print "p[arent is",p
for _ in xrange(int(raw_input())):
	u,v=map(int,raw_input().split())
	m=dfs(u-1)
	n=dfs(v-1)
	print m
	print n
