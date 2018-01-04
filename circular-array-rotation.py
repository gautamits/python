n,k,q=map(int,raw_input().split())
arr=map(int,raw_input().split())
k=k%(2*n)
if k==len(arr):
    arr=arr[::-1]
elif k > n:
    k=k-n
    arr=arr[::-1]
    arr=arr[n-k:]+arr[:n-k]
elif k==0:
    pass
else:
    arr=arr[n-k:]+arr[:n-k]
#print arr
for _ in xrange(q):
    print arr[int(raw_input())]
