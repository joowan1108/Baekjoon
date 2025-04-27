def solution(prices):
    """
    순회-> 작아지는 시점을 구한다. 그때 뒤 애들을 비교
    """
    stack = [0]
    times = [0]*len(prices)
    for i in range(1,len(prices)):
        while stack and prices[stack[-1]]>prices[i]:
            tmp = stack.pop()
            times[tmp]=i-tmp
        stack.append(i)
    
    while stack:
        tmp = stack.pop()
        times[tmp]=len(prices)-tmp-1
    return times
            
        
                
           
        
        
        