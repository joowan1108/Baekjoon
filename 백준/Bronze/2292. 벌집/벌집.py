import sys

input = sys.stdin.readline

#6(6*1) 18(6*3) 36(6*6) 60(6*10)

n = int(input())
i=1
add=2
layer=2
while True:
    if(n-1<=6*i):
        break
    else:
        i+=add
        add+=1
        layer+=1

if(n==1):
    print(1)
else:
    print(layer)

    
    
    
    