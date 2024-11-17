import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = []
for _ in range(n):
	nums.append(list(map(int, input().split())))
	
visited = [[False]*m for _ in range(n)]
max_=0
moves = [(-1,0), (1,0), (0,-1), (0,1)]

num_maximum = 0
for i in range(n):
    for j in range(m):
        if num_maximum < nums[i][j]:
            num_maximum = nums[i][j]
        

def dfs(current, val, cnt):
	global max_
	if(max_ >= val+(4-cnt)*num_maximum):
		return
	if(cnt==4):
		max_ = max(max_, val)
		return
	for y,x in current:
		for dy, dx, in moves:
			new_y, new_x = y+dy, x+dx
			if(0<=new_y<n and 0<=new_x<m and not visited[new_y][new_x]):
				visited[new_y][new_x]=True
				dfs(current+[(new_y, new_x)], val+nums[new_y][new_x], cnt+1)
				visited[new_y][new_x]=False
	
for i in range(n):
	for j in range(m):
		visited[i][j]=True
		dfs([(i,j)], nums[i][j], 1)
	

print(max_)
		
		
		
		
		
		