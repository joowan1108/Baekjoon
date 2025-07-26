import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

answer = 0
start = 1
end = n**2
while start <= end:
  mid = (start+end)//2
  small_equal_cnt = 0
  for i in range(1,n+1):
    small_equal_cnt += min(mid//i, n)

  if small_equal_cnt < k:
    start = mid+1
  else:
    end = mid-1
    answer = mid
print(answer)
      
      
    


