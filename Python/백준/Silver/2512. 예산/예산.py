import sys
input = sys.stdin.readline

n = int(input())
regions = list(map(int, input().split()))
  
total = int(input())
ans = 0

need = sum(regions)
if need < total:
  print(max(regions))

else:
  #지급해야 할 최대 상한액을 구해야 한다
  end = max(regions)
  start = 0
  while start<=end:
    total_given = 0
    mid = (start+end)//2
    for r in regions:
      if r <= mid:
        total_given += r
      else:
        total_given += mid
    
    #상한액이 너무 클 때
    if total_given > total:
      end = mid-1

    #상한액이 적을 때
    else:
      start = mid+1
      ans = mid
  
    
  print(ans)



    
  




