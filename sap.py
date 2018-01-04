
for _ in xrange(int(raw_input())):
	raw_input()
	arr=map(int,raw_input().split())
	subarrays=[]
	for i in xrange(1,len(arr)):
		j=0
		while j < len(arr) and j+i <= len(arr):
			subarrays.append(arr[j:j+i])
			j+=1
	count=0
	for i in subarrays:
		if min(i)==max(i):
			count+=1
	print count
