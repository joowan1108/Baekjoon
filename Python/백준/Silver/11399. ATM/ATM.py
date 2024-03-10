N = int(input())
timetake = list(map(int, input().split()))

timetake.sort()
total_time = []
total=0
for t in timetake:
    total+=t
    total_time.append(total)
print(sum(total_time))