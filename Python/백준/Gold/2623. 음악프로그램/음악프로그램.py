import sys
import heapq
input = sys.stdin.readline

'''
topological sort를 하여 inorder가 모두 동일한 경우에는 불가능하고 그렇지 않다면 계속 진행
'''

n,m = map(int, input().split())
inorder = [0]*(n+1)
graph = [[] for _ in range(n+1)]
cycle = False

for _ in range(m):
  orders = list(map(int, input().split()))
  for i in range(2,orders[0]+1):
    inorder[orders[i]]+=1
    graph[orders[i-1]].append(orders[i])


q = []
for i in range(1,n+1):
  if inorder[i]==0:
    heapq.heappush(q, (0,i))

result = []
visited = set()
while q:
  ins, num = heapq.heappop(q)
  if num in visited:
    continue
  visited.add(num)
  result.append(num)
  for adj in graph[num]:
    inorder[adj]-=1
    if inorder[adj] == 0:
      heapq.heappush(q, (0,adj))

#우선순위가 0이 아니면서 동일해서 순위가 안 정해졌는지 보는 방법
for i in range(1,n+1):
  if inorder[i] != 0:
    cycle = True
    

if cycle:
  print(0)
else:
  for r in result:
    print(r)
    
        
        
    

        
      
    
    
  

  
