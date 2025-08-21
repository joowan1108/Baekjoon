import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
  n = int(input())
  stickers = []
  for _ in range(2):
    stickers.append(list(map(int, input().split())))
  
  for j in range(1,n):
    stickers[0][j] = max(stickers[0][j]+stickers[1][j-1], stickers[0][j-1])
    stickers[1][j] = max(stickers[1][j]+stickers[0][j-1], stickers[1][j-1])
  ans.append(max(stickers[0][n-1], stickers[1][n-1]))

for i in range(T):
  print(ans[i])





