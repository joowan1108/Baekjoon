import sys
import heapq
input = sys.stdin.readline

T = int(input())

"""
전부 sort
맨 위는 서류 등수가 제일 낮은애
이제 i번째 사람은 0~i-1번의 모든 사람들보다 면접 등수가 낮으면 된다 --> 채용
"""

for _ in range(T):
  n = int(input())
  scores = []
  for _ in range(n):
    a,b = map(int, input().split())
    scores.append((a,b))
  scores.sort()
  interview_min = scores[0][1]
  cnt = 1
  for i in range(1,n):
    if scores[i][1] < interview_min:
      interview_min = scores[i][1]
      cnt+=1
  print(cnt)

  
  
      
  
      
    
      
    
  