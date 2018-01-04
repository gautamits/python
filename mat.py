def moveup(a):
	index=a.index(0)
	if index in [0,1,2]:
		return -1
	else:
		a[index],a[index-3]=a[index-3],a[index]
		return a
def movedown(a):
	index=a.index(0)
	if index in [6,7,8]:
		return -1
	else:
		a[index],a[index+3]=a[index+3],a[index]
		return a
def moveleft(a):
	index=a.index(0)
	if index in [0,3,6]:
		return -1
	else:
		a[index],a[index-1]=a[index-1],a[index]
		return a
def moveright(a):
	index=a.index(0)
	if index in [2,6,8]:
		return -1
	else:
		a[index],a[index+1]=a[index+1],a[index]
		return a



result=[1,2,3,4,5,6,7,8,0]
arr=[]
l=[]
print "enter array"
arr.append(map(int,raw_input().split()))
l.append(arr)
while(len(l)>0):
	a=l.pop()
	if a==result:
		print "got it"
		exit()
	else:
		up=moveup(a)
		if up!=-1 and up not in l:
			l.append(up)
		down=movedown(a)
		if down!=-1 and down not in l:
			l.append(down)
		left=moveleft(a)
		if left!=-1 and left not in l:
			l.append(left)
		right=moveright(a)
		if right!=-1 and right not in l:
			l.append(right)
print "not solvable"
		
