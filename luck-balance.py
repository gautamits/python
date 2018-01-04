l,k=raw_input().split()
l=int(l)
k=int(k)
weightage=[]
importance=[]
total=0
for i in xrange(l):
	a,b=raw_input().split()
	if b=="1":
		weightage.append(int(a))
	else:
		total=total+int(a)
weightage=sorted(weightage)
weightage=weightage[::-1]
print total+sum(weightage[:k])-sum(weightage[k:])

