import heapq, sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
	tmp = int(input())
	if(tmp>0):
		heapq.heappush(heap, tmp)
	else:
		if(len(heap)==0):
			print(0)
		else:
			print(heapq.heappop(heap))
		