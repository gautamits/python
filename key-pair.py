for i in range(int(raw_input()):
    a,b=map(int,raw_input().split())
    arr=map(int,raw_input().split())
    for j in range(a):
        if b-arr[j] in arr:
            print 'YES'
            break
        elif j==a-1:
            print 'NO'
