import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

"""
경로가 unique해야하므로 방향들도 다 저장해놓아야함

각 칸에 도달 횟수를 저장 -> dp
"""


n = int(input())
maps = []
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
#[y][x][c]: y,x를 c 방향으로 온 경우의 수
for _ in range(n):
  maps.append(list(map(int, input().split())))

dp[0][1][0] = 1

for y in range(n):
  for x in range(2,n):
    if maps[y][x] == 1:
      continue
    #가로로 도착
    dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
    #세로로 도착
    if y-1>=0:
      dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
    #대각선으로 도착
    if y-1>=0 and x-1>=0 and maps[y-1][x] != 1 and maps[y][x-1] != 1:
      dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[n-1][n-1]))

        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  