n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))
coords.sort(key=lambda t:(t[1], t[0]))
for i in range(n):
    print("{} {}".format(coords[i][0], coords[i][1]))
    