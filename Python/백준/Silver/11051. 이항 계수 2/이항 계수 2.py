import sys
import  math
input = sys.stdin.readline

n, k = map(int, input().split())

"""
nCk = n-1Ck-1 + n-1Ck
"""

combs = [[0]*(n+1) for _ in range(n+1)]
#combs[j][i] = iCj

combs[1][1] = 1
combs[0][1] = 1
for i in range(n+1):
  combs[i][i]=1
  
for i in range(1,n+1):
  for j in range(i+1):
    combs[j][i] = (combs[j-1][i-1] + combs[j][i-1])%10007

print(combs[k][n]%10007)
    
