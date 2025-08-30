import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
  s,t = map(int, input().split())
  classes.append((s,t))

"""
수업 시작 시간이 빠른 애들부터 강의실 배정

이때 그 중에 끝나는 시간이 빠른 애들도 강의실을 빨리 배정해야함 -> 그래야지 다음 수업이 더 빨리 시작할 수 있게됌

"""

end_times = []
classes.sort(key = lambda x: x[1])
classes.sort(key = lambda x: x[0])
rooms = 1 #처음 애는 배정
heapq.heappush(end_times, classes[0][1])
#print(f"classes: {classes}")
for i in range(1,n):
  #print(end_times)
  end = heapq.heappop(end_times)
  if classes[i][0] >= end:
    heapq.heappush(end_times, classes[i][1])
  else:
    heapq.heappush(end_times, end)
    heapq.heappush(end_times, classes[i][1])
    rooms += 1
    

print(rooms)
    
    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  