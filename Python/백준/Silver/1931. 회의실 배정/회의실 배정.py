import sys
input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
	a,b = map(int, input().split())
	times.append((a,b))

times = sorted(times, key=lambda x: (x[1], x[0]))
start = 0
end = 0
cnt = 0
for x,y in times:
	if(x>=end):
		cnt+=1
		end = y

print(cnt)
	