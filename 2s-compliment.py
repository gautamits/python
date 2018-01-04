for _ in range(int(raw_input())):
    a,b=raw_input().split()
    a=int(a)
    b=int(b)
    count=0
    print a,b
    while a < 0:
        print a,32-bin(-a).count("1")
        count=count+ (32-bin(-a).count("1"))
        a+=1
    print count
    print count