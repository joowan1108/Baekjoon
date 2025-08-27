import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

"""
제일 큰 것을 고르는 것은 잔돈을 적게 주는 goal과 같음

동전의 개수가 무한이기에 서로의 선택이 영향을 주지 않음 --> greedy
"""

money = int(input())
money = 1000 - money

coins = [500,100,50,10,5,1]
ans = 0
for coin in coins:
  if money >= coin:
    cnt = money//coin
    money -= coin*cnt
    ans+=cnt
  else:
    continue

print(ans)

  
      
        
    
  
