import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums_copy = nums.copy()
nums_copy = list(set(nums_copy))
nums_copy.sort()

def binarysearch(target):
	start = 0
	end = len(nums_copy)-1
	while start<=end:
		mid = (start+end)//2
		if(nums_copy[mid]==target):
			return mid
		elif(nums_copy[mid]>target):
			end = mid-1
		else:
			start = mid+1
		
	
for num in nums:
	print(binarysearch(num), end=' ')
	

        