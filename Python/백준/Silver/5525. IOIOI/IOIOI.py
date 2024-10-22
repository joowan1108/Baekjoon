import sys
input = sys.stdin.readline

p = 'I'
n = int(input())
for _ in range(n):
	p=p+'O'+'I'
	
m = int(input())
s = input().rstrip()

start = 0
end = 2*n
cnt=0

while end<m:
	window = s[start:end+1]
	if(window==p):
		cnt+=1
	start+=1
	end+=1

print(cnt)