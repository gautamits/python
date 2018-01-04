from itertools import combinations,permutations
for _ in xrange(int(raw_input())):
    s=raw_input()
    if s=="0":
        print "1"
        continue
    elif "0" in s and ( s.count("0")==2 or "2" in s or "4" in s):
        print "1"
        continue
    elif "1" in s and ( "2" in s or "6" in s):
        print "1"
        continue
    elif "2" in s and ( "4" in s or "8" in s or "3" in s):
        print "1"
        continue
    elif "3" in s or "6" in s:
        print "1"
        continue
    else:
        print "0"
