import os
handle=file("dup","r")
temp=handle.read()
temp=temp.split('\n\n')
for j in temp:
	k=j.split('\n')
	n=len(k)
	print n
	z=1
	while z < n:
		os.remove('/home/amit/'+k[z])
