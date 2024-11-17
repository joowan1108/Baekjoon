import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

blocks = []
for _ in range(n):
	blocks.append(list(map(int, input().split())))
	
max_h = 0
min_ = float("inf")
for i in range(n):
	for j in range(m):
		max_h = max(max_h, blocks[i][j])

for h in range(max_h+1):
	blocks_used = 0
	blocks_removed = 0
	for i in range(n):
		for j in range(m):
			if blocks[i][j]<h:
				blocks_used+=h-blocks[i][j]
			else:
				blocks_removed+=blocks[i][j]-h
	if blocks_used > b+blocks_removed:
		continue
	time = blocks_used + 2*blocks_removed
	
	if time<=min_:
		min_ = time
		level = h

print(min_, level)
	

				
				
	
		
		
		
		
		
		