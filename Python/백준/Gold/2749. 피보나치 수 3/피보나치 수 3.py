import sys
input = sys.stdin.readline

n = int(input())

memo = dict()
memo[0] = 0
memo[1] = 1
memo[2] = 1

def fibo(k):
  if k in memo:
    return memo[k]
  else:
    if k%2==0:
      m = k//2
      f_1 = fibo(m)%1000000
      f_2 = fibo(m+1)%1000000
      f = f_1 * ((2*f_2 - f_1)) %1000000
      memo[k] = f
      return f
    else:
      m = k//2
      f_1 = (fibo(m))**2%1000000
      f_2 = (fibo(m+1))**2%1000000
      f = ((f_1) + (f_2)) %1000000
      memo[k] = f
      return f%1000000

print(fibo(n)%1000000)