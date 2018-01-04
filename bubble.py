arr=map(int,raw_input().split())
n=len(arr)
for i in range(n):
	for j in range(i,n):
		if arr[i] > arr[j]:
			arr[i],arr[j]=arr[j],arr[i]
print arr