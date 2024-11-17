import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

blocks = dict()
for _ in range(n):
	line = list(map(int, input().split()))
	for l in line:
		if l in blocks:
			blocks[l]+=1
		else:
			blocks[l]=1
	
max_h = max(blocks.keys())
min_h = min(blocks.keys())

min_ = float("inf")
level = 0

for h in range(min_h, max_h+1):
	blocks_used = 0
	blocks_removed = 0
	for height, num in blocks.items():
		if height>h:
			blocks_removed +=(height-h)*num
		else:
			blocks_used +=(h-height)*num
	if blocks_used > b+blocks_removed:
		continue
	time = blocks_used + 2*blocks_removed
	
	if time<=min_:
		min_ = time
		level = h

print(min_, level)
	

				
				
	
		
		
		
		
		
		