import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
	k = int(input())
	exist_both = [False]*(1000001)
	min_heap = []
	max_heap = []
	for v in range(k):
		inst, num = input().rstrip().split()
		num = int(num)
		
		if inst=='I':
			exist_both[v]=True
			heapq.heappush(min_heap, (num,v))
			heapq.heappush(max_heap, (-num,v))
		else:
			if num==1:
				while max_heap and not exist_both[max_heap[0][1]]:
					heapq.heappop(max_heap)
				if max_heap:
					exist_both[max_heap[0][1]]=False
					heapq.heappop(max_heap)
			else:
				while min_heap and not exist_both[min_heap[0][1]]:
					heapq.heappop(min_heap)
				if min_heap:
					exist_both[min_heap[0][1]]=False
					heapq.heappop(min_heap)
	
	while max_heap and not exist_both[max_heap[0][1]]:
		heapq.heappop(max_heap)
	while min_heap and not exist_both[min_heap[0][1]]:
		heapq.heappop(min_heap)
	if max_heap and min_heap:
		print(f"{-max_heap[0][0]} {min_heap[0][0]}")
	else:
		print("EMPTY")
		