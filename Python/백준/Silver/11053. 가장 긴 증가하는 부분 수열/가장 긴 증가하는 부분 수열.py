import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

length = [1 for _ in range(n)]

for i in range(n):
	for j in range(i):
		if seq[i]>seq[j]:
			length[i]=max(length[i], length[j]+1)		

print(max(length))

		
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
