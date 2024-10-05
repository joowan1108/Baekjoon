import sys
input = sys.stdin.readline
def getRounded(num):
    if (num-int(num)>=0.5):
        return int(num+1)
    else:
        return int(num)

n = int(input().strip())

difficulty = []
for _ in range(n):
    difficulty.append(int(input().strip()))

if(n==0):
    print(0)
else:
    difficulty.sort()
    nums_eliminated = getRounded(n*0.15)
    difficulty = difficulty[nums_eliminated:n-nums_eliminated]
    
    average = getRounded(sum(difficulty)/(n-2*nums_eliminated))
    
    print(average)
            
        
        
                    
                    
        
    