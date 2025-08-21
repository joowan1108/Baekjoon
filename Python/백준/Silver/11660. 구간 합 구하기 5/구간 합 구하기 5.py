import sys
input = sys.stdin.readline

n,m = map(int, input().split())

square = []
square.append([0]*(n+1))

for _ in range(n):
  square.append([0]+list(map(int, input().split())))

queries = []
for _ in range(m):
  queries.append(list(map(int, input().split())))

"""
각 행들을 prefix sum으로 바꾸기
h1~h2까지 각 행[w2]-행[w1]을 한다
h1과 h2가 같을 때랑, w1랑 w2가 같을 때랑 예외 구분해야함
=시간초과

2차원 prefix sum을 만든 후 a4 = (a1+a2+a3+a4) - (a1+a3) - (a1+a2) + a1임을 이용
"""

#가로 prefix sum
for h in range(1,n+1):
  for w in range(1,n+1):
    square[h][w] += square[h][w-1]
#세로 prefix sum
for h in range(1,n+1):
  for w in range(1,n+1):
    square[h][w] += square[h-1][w]
    
for query in queries:
  h1,w1,h2,w2 = query
  ans = square[h2][w2] - (square[h2][w1-1]) - (square[h1-1][w2]) + square[h1-1][w1-1]

  print(ans)






  
  

