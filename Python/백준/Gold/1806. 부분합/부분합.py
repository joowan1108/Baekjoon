import sys
input = sys.stdin.readline


"""

prefix sum으로도 모든 길이에 대한 경우의 수를 구하려면 N^2이 걸림
-> 최소 길이 iteration을 binary search로 한다면 NlogN으로 구할 수 있음
"""

n,s = map(int, input().split())
nums = [0] + list(map(int, input().split()))
prefix_sum = [0]*(n+1)

for i in range(1,n+1):
  prefix_sum[i] = prefix_sum[i-1] + nums[i]

start = 1
end = n
ans = int(1e9)
while start <= end:
  mid = (start+end)//2
  found = False
  for j in range(n+1-mid):
    sum_ = prefix_sum[j+mid] - prefix_sum[j]
    if sum_ >= s:
      found = True
      break
  #mid 길이로 s가 된다면, 더 짧은 길이 시도
  if found:
    end = mid-1
    ans = min(ans, mid)
  else:
    start = mid+1

if ans == int(1e9):
  print(0)
else:
  print(ans)
      
      
      














