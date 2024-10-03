import sys
input = sys.stdin.readline

def getFact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*getFact(n-1)

num = int(input())
fact = list(str(getFact(num)))
fact.reverse()

count=0
for i in range(len(fact)):
    if(fact[i]=='0'):
        count+=1
    else:
        break

print(count)

        
        


        
