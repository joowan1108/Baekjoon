import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	p = input().rstrip()
	n = int(input())
	nums = input().rstrip()
	nums = nums[1:-1]
	nums = nums.split(',')
	arr = deque(nums)
	if(n==0):
		arr = []
	error = False
	cnt_r = 0
	for instruction in p:
		if(instruction=='R'):
			cnt_r+=1
		else:
			if(len(arr)>0):
				if(cnt_r%2==0):
					arr.popleft()
				else:
					arr.pop()
			else:
				error =True
				break
		
	if(error):
		print('error')
	else:
		arr = list(arr)
		if(cnt_r%2==0):
			print("["+",".join(arr)+"]")
		else:
			arr.reverse()
			print("["+",".join(arr)+"]")
		
			
			