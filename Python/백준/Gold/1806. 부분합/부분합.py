import sys
input = sys.stdin.readline

n,s = map(int, input().split())
nums = [0] + list(map(int, input().split()))


prefix_sum = [0]*(n+1)
for i in range(1,n+1):
  prefix_sum[i] = prefix_sum[i-1] + nums[i]

start, end = 0,1
ans = int(1e9)
while start <= end and end<=n:
  if prefix_sum[end] - prefix_sum[start] < s:
    end += 1
  else:
    ans = min(ans,end - start)
    start += 1

if ans == int(1e9):
  print(0)
else:
  print(ans)
    
  
