import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lectures = list(map(int, input().split()))


ray_start = max(lectures)
ray_end = sum(lectures)
ans = ray_end

while ray_start <= ray_end:
  ray_size = (ray_start + ray_end)//2
  total = 0
  cnt=1

  for lecture in lectures:
    if total + lecture > ray_size:
      cnt+=1
      total = lecture
    else:
      total+=lecture


  #최소 길이 구하기
  if cnt<=m:
    ans = ray_size
    ray_end = ray_size-1


  else:
    ray_start = ray_size+1


print(ans)