import re
def isprime(n):
	return not re.match(r'^.?$|^(..+?)\1+$','1'*n)
for i in range(100):
	print i,isprime(i)
