import sys

def lcs(X,Y):
	ans=[]
	m=len(X)
	n=len(Y)
	L= [[None]*(n+1) for i in xrange(m+1)]
	print L
	for i in xrange(m+1):
		for j in xrange(n+1):
			if i==0 or j==0:
				L[i][j]=0
			elif X[i-1] == Y[j-1]:
				L[i][j]=L[i-1][j-1]+1
			else:
				L[i][j]=max(L[i-1][j],L[i][j-1])
	print L
				
	return L[m][n]
print lcs(sys.argv[1],sys.argv[2])
