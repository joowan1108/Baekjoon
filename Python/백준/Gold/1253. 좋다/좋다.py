import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0
for i,num in enumerate(nums):
  target = num
  target_list = nums[:i] + nums[i+1:]
  start = 0
  end = len(target_list)-1
  while start < end:
    addition = target_list[start] + target_list[end]
    if addition > target:
      end-=1
    elif addition < target:
      start+=1
    else:
      ans+=1
      break
    
print(ans)
