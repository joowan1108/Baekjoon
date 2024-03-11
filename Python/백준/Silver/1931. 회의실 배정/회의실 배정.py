n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s,e))
times = sorted(times, key = lambda x:(x[1], x[0]))
cnt = 1
idx=0
for i in range(idx+1, n):
    if(times[idx][1] <= times[i][0]):
        cnt+=1
        idx=i
    
print(cnt)
    