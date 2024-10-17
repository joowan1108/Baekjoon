import sys

input = sys.stdin.readline

n,m = map(int, input().split())

nums = list(map(int, input().split()))
for i in range(1,len(nums)):
	nums[i]=nums[i]+nums[i-1]
	
for _ in range(m):
	start, end = map(int, input().split())
	end-=1
	start-=1
	if(start==0):
		print(nums[end])
	else:
		print(nums[end]-nums[start-1])
	
	
	

	

