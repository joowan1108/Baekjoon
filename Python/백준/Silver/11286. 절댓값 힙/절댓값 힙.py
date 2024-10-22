import sys
import heapq

input = sys.stdin.readline

heap_pos = []
heap_neg = []

n = int(input())
for _ in range(n):
	x = int(input())
	if(x!=0):
		if(x>0):
			heapq.heappush(heap_pos, x)			
		else:
			heapq.heappush(heap_neg, -x)
	else:
		if(len(heap_pos)+len(heap_neg)==0):
			print(0)
		else:
			if(len(heap_pos)>0 and len(heap_neg)>0):
				pos = heapq.heappop(heap_pos)
				neg = -heapq.heappop(heap_neg)
				if(abs(pos)>=abs(neg)):
					print(neg)
					heapq.heappush(heap_pos, pos)
				else:
					print(pos)
					heapq.heappush(heap_neg, -neg)
			elif(len(heap_pos)>0):
				print(heapq.heappop(heap_pos))
			else:
				print(-heapq.heappop(heap_neg))
		
		