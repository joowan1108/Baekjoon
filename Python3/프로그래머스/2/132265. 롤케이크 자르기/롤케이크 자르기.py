from collections import Counter

def solution(topping):
    
    cnt = 0
    
    toppings = Counter(topping)
    
    half = set()
    
    for top in topping:
        half.add(top)
        toppings[top]-=1
        if toppings[top]==0:
            toppings.pop(top)
        
        if len(toppings) == len(half):
            cnt+=1
    
    return cnt
            
        
    