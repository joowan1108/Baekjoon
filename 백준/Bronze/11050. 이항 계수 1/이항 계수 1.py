import sys

input = sys.stdin.readline

n,k=map(int, input().split())

def getFact(num):
    if(num==1 or num==0):
        return 1
    return num*getFact(num-1)

print(int(getFact(n)/(getFact(k)*getFact(n-k))))

    
    