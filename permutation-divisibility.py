from itertools import combinations,permutations
for _ in xrange(int(raw_input())):
	s=raw_input()
	p=list(set("".join(i) for i in permutations(s,2)))
	for i in xrange(len(p)):
		if int(p[i]) % 4 ==0:
			print 1
			break
		else:
			if i==len(p)-1:
				print 0
				break
			else:
				continue
