import sys
input = sys.stdin.readline

t = int(input())

case = [0]*11
case[1]=1
case[2]=2
case[3]=4
for i in range(4, len(case)):
	case[i]=case[i-3]+case[i-2]+case[i-1]
	
for _ in range(t):
	n = int(input())
	print(case[n])



