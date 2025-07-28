import sys
import math
input = sys.stdin.readline

x,y = map(int, input().split())

def get_winrate(games,wins):
  return int((100*wins/games))

def is_different(a,b):
  return True if a!=b else False


z = get_winrate(x,y)
ans = 0 

if z >= 99:
  print(-1)

else:
  start = 1
  end = x
  while start <= end:
    mid = (start+end)//2
    new_z = get_winrate(x+mid, y+mid)
    if is_different(new_z, z):
      end = mid-1
      ans = mid
    else:
      start = mid+1
  print(ans)
    


