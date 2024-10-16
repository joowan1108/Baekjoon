import sys

input = sys.stdin.readline
n,k = map(int, input().split())

coin_val = []
for _ in range(n):
	coin_val.append(int(input()))

coin_val.reverse()

total=0
for c in coin_val:
	num = k//c
	total+=num
	k = k-num*c
	
print(total)
		
	
	
        