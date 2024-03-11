n = int(input())
coords = []
for _ in range(n):
    lst = list(map(int, input().split()))
    x,y = lst[0], lst[1]
    coords.append((x,y))

result = sorted(coords)
for i in range(n):
    print("{} {}".format(result[i][0], result[i][1]))