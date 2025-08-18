import sys
input = sys.stdin.readline

n = int(input())
pos = []
neg = []
result = 0
for _ in range(n):
  num = int(input())
  if num>1:
    pos.append(num)
  elif num==1:
    result+=1
  else:
    neg.append(num)

pos.sort(reverse=True)
neg.sort()

i=0
while i<(len(pos)-1):
  result += pos[i]*pos[i+1]
  i+=2
if i==len(pos)-1:
  result+=pos[i]

j=0
while j<(len(neg)-1):
  result += neg[j]*neg[j+1]
  j+=2
if j==len(neg)-1:
  result+=neg[j]

print(result)
      
    
    
    
    

  

    
    
    




  
    