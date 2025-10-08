import sys
input = sys.stdin.readline

n,m = map(int, input().split())
test = []

for _ in range(n):
  test.append(int(input()))

start = min(test)
end = max(test) * m


"""
전체 걸릴 수 있는 모든 시간 경우의 수에서 최적의 경우의 수를 찾는 이진 탐색을 하면 된다.
"""
ans = 0
while start <= end:
  complete = 0
  mid = (start+end)//2
  for t in test:
    complete += mid // t
  #시간이 너무 충분할 때
  if complete >= m:
    end = mid-1
    ans = mid
  else:
    start = mid+1

print(ans)
    
  
  
  

