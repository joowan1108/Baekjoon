import sys
from collections import deque

input = sys.stdin.readline

a,b = map(int, input().split())

def bfs(start):
	q = deque()
	q.append((start,1))
	while q:
		tmp,cnt = q.popleft()
		if tmp==b:
			print(cnt)
			return
		if tmp*2<=b:
			q.append((tmp*2, cnt+1))
		if int(str(tmp)+'1')<=b:
			q.append((int(str(tmp)+'1'), cnt+1))
	print(-1)
		

bfs(a)



		
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
