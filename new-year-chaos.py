for _ in xrange(int(raw_input())):
    n=raw_input()
    chaotic=False
    count=0
    arr=map(int,raw_input().split())
    for i in xrange(len(arr)):
        diff=arr[i]-(i+1)
        #print diff
        if diff>0:
            count+=diff
        if diff>2:
            chaotic=True
            break
    if chaotic==True:
        print "Too chaotic"
    else:
        print count
