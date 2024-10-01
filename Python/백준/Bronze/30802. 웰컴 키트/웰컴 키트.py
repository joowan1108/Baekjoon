# Online Python-3 Compiler (Interpreter)
import sys
import math
input = sys.stdin.readline

N = int(input())

sizes = list(map(int, input().split()))

groups = list(map(int, input().split()))
t = groups[0]
p=groups[1]
#티셔츠 개수 구하기
tshirtnum=0
def getShirt(i):
    if(i==0):
        return 0
    elif(i<=t):
        return 1
    else:
        if(i%t==0):
            return i//t
        else:
            return i//t+1
for size in sizes:
    tshirtnum+=getShirt(size)
print(tshirtnum)
#펜 수 구하기
indiv = N%p
group = N//p
print(f"{group} {indiv}")
    