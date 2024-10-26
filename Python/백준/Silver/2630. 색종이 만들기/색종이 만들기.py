import sys
input = sys.stdin.readline

n = int(input())

paper = []
color_num = [0,0]
for _ in range(n):
	paper.append(list(map(int, input().split())))

def check(y_start, x_start, N):
	tmp = paper[y_start][x_start]
	for i in range(y_start, y_start+N):
		for j in range(x_start, x_start+N):
			if (tmp!=paper[i][j]):
				check(y_start, x_start, N//2)
				check(y_start, x_start+N//2,N//2)
				check(y_start+N//2,x_start,N//2)
				check(y_start+N//2, x_start+N//2,N//2)
				return
	color_num[tmp]+=1

check(0,0,n)
for c in color_num:
	print(c)