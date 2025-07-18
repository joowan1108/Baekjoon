import sys
input = sys.stdin.readline

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
start_team = [False]*(n)

min_ = int(1e9)



def backtrack(iter, start):
  global min_
  if iter == n//2:
    start_score = 0
    link_score = 0
    #점수 계산
    for i in range(n):
      for j in range(n):
        if start_team[i] and start_team[j]:
          start_score += S[i][j]
        elif not start_team[i] and not start_team[j]:
          link_score += S[i][j]
    min_ = min(min_, abs(start_score - link_score))
    return


  for i in range(start, n):
    if not start_team[i]:
      start_team[i] = True
      backtrack(iter+1, i+1)
      start_team[i] = False

backtrack(0, 0)
print(min_)