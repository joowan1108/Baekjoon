import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

"""
비어있는 좌표들을 다 iterate 하면서 backtracking.
이때 모든 좌표들에 대해 check가 다 완료되었다면 그 즉시 끝내기
"""
empty_coords = [(i,j) for i in range(9) for j in range(9) if board[i][j]==0]
coords = len(empty_coords)

def check(h,w, num):
  for i in range(9):
    if board[h][i] == num or board[i][w] == num:
      return False
  
  h_= (h//3)*3
  w_ = (w//3)*3
  for i in range(3):
    for j in range(3):
      if board[h_+ i][w_ + j] == num:
        return False
  return True
  
def backtrack(iter):
  #탐색하는 가지를 줄여야한다
  if iter == coords:
    for row in board:
      print(*row)
    sys.exit()

  h,w = empty_coords[iter]
  for i in range(1,10):
    if check(h,w,i):
      board[h][w]=i
      backtrack(iter+1)
      board[h][w]=0

backtrack(0)





