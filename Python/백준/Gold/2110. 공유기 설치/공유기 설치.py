import sys
input = sys.stdin.readline

n,c = map(int, input().split())

coords = []
for _ in range(n):
  coords.append(int(input()))

coords.sort()
result = 0
start = 1
end = coords[-1] - coords[0]

while start<=end:
  mid = (start+end)//2
  select = coords[0]
  cnt = 1
  for i in range(n):
    if coords[i] >= select + mid:
      select = coords[i]
      cnt+=1
  if cnt >= c:
    #거리를 늘려야함
    start = mid+1
    result = mid
  else:
    #거리를 좁혀야함
    end = mid-1

print(result)




    
  




