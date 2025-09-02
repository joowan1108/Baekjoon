import sys
input = sys.stdin.readline

n = int(input())

n1, n2, n3 = map(int, input().split()) 
max_add1, max_add2, max_add3 = n1, n2, n3
min_add1, min_add2, min_add3 = n1, n2, n3
for _ in range(1,n):
    n1, n2, n3 = map(int, input().split()) 
    max1 = n1 + max(max_add1, max_add2)
    max2 = n2 + max([max_add1, max_add2, max_add3])
    max3 = n3 + max(max_add2, max_add3)
    max_add1 = max1
    max_add2 = max2
    max_add3 = max3

    min1 = n1 + min(min_add1, min_add2)
    min2 = n2 + min([min_add1, min_add2, min_add3])
    min3 = n3 + min(min_add2, min_add3)
    min_add1 = min1
    min_add2 = min2
    min_add3 = min3

print(f"{max([max_add1, max_add2, max_add3])} {min([min_add1, min_add2, min_add3])}")
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  