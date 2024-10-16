import sys

input = sys.stdin.readline

x = int(input())
opers = [0 for _ in range(0,1000001)]

opers[1]=0
opers[2]=1
opers[3]=1
for i in range(4,len(opers)):
	opers[i] = opers[i-1]+1
	if(i%2==0):
		opers[i]=min(opers[i], opers[i//2]+1)
	if(i%3==0):
		opers[i]=min(opers[i], opers[i//3]+1)
		
print(opers[x])



		
	
		
	
	
        