import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
  ropes.append(int(input()))

ropes.sort(reverse=True)
"""
무거운 ropes부터 시작
ans 변수에는 고른 ropes 중 제일 작은것 * 고른 ropes 개수가 들어간다
"""
ans = 0

for i in range(n):
  ans = max(ans, ropes[i]*(i+1))

print(ans)
  

    
    
    




  
    