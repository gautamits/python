import math
n=int(raw_input("enter the number to check for multiplicity of 3\n"))
n=bin(n)[2:]
n=n[::-1]
print n
even=0
odd=0
count=0
for i in n:
	if count==0:
		even+=int(i)
	else:
		odd+=int(i)
	count^=1
print bool(abs(even-odd)%3^1)