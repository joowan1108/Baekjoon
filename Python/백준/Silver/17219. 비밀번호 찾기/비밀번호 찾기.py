import sys

input = sys.stdin.readline
n,m = map(int, input().split())
password = dict()

for _ in range(n):
	x,y = input().rstrip().split()
	password[x]=y

for _ in range(m):
	q = input().strip()
	print(password[q])
	
		
	
	
        