from collections import Counter
n=int(raw_input())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
a=sorted(a)
b=sorted(b)
counta=Counter(a)
countb=Counter(b)
seta=set(a)
setb=set(b)
print counta
print countb
print seta
print setb
for i in seta.intersection(setb):
    freqa=counta[i]
    freqb=countb[i]
    if freqa < freqb:
        counta[i]=0
        countb[i]=countb[i]-freqa
    else:
        countb[i]=0
        counta[i]=counta[i]-freqb
print counta
print countb
suma=0
sumb=0
for k,v in counta.iteritems():
    suma=suma+k*v
for k,v in countb.iteritems():
    sumb=sumb+k*v
print suma, sumb
