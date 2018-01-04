def hamming(a,b):
	print a,b
	count=0
	for i,j in zip(a,b):
		if i!=j:
			count+=1
	return count



n=raw_input()
arr=list(raw_input())
a=int(raw_input())
for i in xrange(a):
    q=raw_input().split()
    if q[0]=="R":
        l=int(q[1])
        r=int(q[2])
        print arr[l:r]
        arr[l-1:r]=arr[l-1:r][::-1]
    elif q[0]=="C":
        l=int(q[1])
        r=int(q[2])
        ch=q[3]
        arr[l-1:r]=ch*len(arr[l-1:r])
    elif q[0]=="S":
        l1=int(q[1])
        r1=int(q[2])
        l2=int(q[1])
        r2=int(q[2])
        arr[l1-1:r1],arr[l2-1:r2]=arr[l2-1:r2],arr[l1-1:r1]
    elif q[0]=="W":
        l=int(q[1])
        r=int(q[2])
        print arr[l-1:r]
    elif q[0]=="H":
    	l1=int(q[1])
    	l2=int(q[2])
    	l=int(q[3])
    	print hamming(arr[l1-1:l1+l],arr[l2-1:l2+l])
    print arr
