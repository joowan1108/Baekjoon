import sys

input = sys.stdin.readline

n,r,c = map(int, input().split())

cnt = 0
nums = 0


	
def recursion(n,r,c):
	if(n==1):
		return 2*r+c
		
	if(r<2**(n-1) and c<2**(n-1)):
		return recursion(n-1, r,c)

	elif(r<2**(n-1) and c>=2**(n-1)):
		return 2**(2*n-2)+recursion(n-1, r,c-2**(n-1))
	
	elif(r>=2**(n-1) and c>=2**(n-1)):
		return 3*(2**(2*n-2))+recursion(n-1,  r-2**(n-1),c-2**(n-1))
	
	else:
		return 2*(2**(2*n-2))+recursion(n-1,  r-2**(n-1),c)

print(recursion(n,r,c))