import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

vertical = [False] * n
diag_right = set()   #y-x = k
diag_left = set()    #y+x = k
ways = 0
"""
위에서부터 place하고 표시
n개를 다 놓았을 때 방법수+1

확인을 놓을 때마다 하기
"""


def backtrack(y):
  global ways
  if y == n:
    ways+=1
    return

  for x in range(n):
      if not vertical[x] and (y-x) not in diag_right and (y+x) not in diag_left:
        vertical[x] = True
        diag_right.add(y-x)
        diag_left.add(y+x)
        backtrack(y+1)
        vertical[x] = False
        diag_right.remove(y-x)
        diag_left.remove(y+x)


backtrack(0)
print(ways)

    
  

