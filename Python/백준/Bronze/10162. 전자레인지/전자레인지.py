import sys
input = sys.stdin.readline


"""
각 버튼은 서로 배수 관계이다. 제일 큰것부터 채워나가도 상관없음.

버튼 누른 횟수가 최소여야 하므로 시간이 큰 애들부터 채워야함

--> greedy
"""

buttons = [300, 60, 10]
cnts = []
T = int(input())
ans = 0
for button in buttons:
  if button <= T:
    cnt = T//button
    cnts.append(cnt)
    T -= cnt*button
  else:
    cnts.append(0)

if T > 0:
  print(-1)
else:
  for c in cnts:
    print(c, end=' ')


  



  
  
      
  
      
    
      
    
  