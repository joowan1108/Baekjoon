import sys
input = sys.stdin.readline

i = 1
while True:
  l,p,v = map(int, input().split())
  if l==0 and p==0 and v==0:
    break

  cnt = v // p
  v -= cnt*p
  days = 0
  days += cnt*l
  days += v if v <= l else l 
  print(f"Case {i}: {days}")
  i+=1

  
    


    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  