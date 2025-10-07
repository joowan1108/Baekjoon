import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

n = int(input())
memo = dict()
memo[0] = 0
memo[1] = 1
memo[2] = 1
def fibo(k):
  if k in memo:
    return memo[k]

  elif k % 2 == 0:
    m = k//2
    f_1 = fibo(m)%1000000007
    f_2 = fibo(m+1)%1000000007
    f = (f_1 * (2 * f_2 - f_1)) %1000000007
    memo[k] = f
    return f

  else:
    m = k // 2
    f_1 = fibo(m)%1000000007
    f_2 = fibo(m+1)%1000000007
    f = (pow(f_1,2)%1000000007 + pow(f_2,2)%1000000007)%1000000007
    return f

print(fibo(n))