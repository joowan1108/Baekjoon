from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerines = sorted(counter.values(), reverse=True)
    
    types = 0
    idx = 0
    
    while True:
        if idx == len(tangerine) or k==0:
            break
            
        if k>=tangerines[idx]:
            types += 1
            k -= tangerines[idx]
            idx+=1
            
        else:
            types+=1
            k=0
            
    return types