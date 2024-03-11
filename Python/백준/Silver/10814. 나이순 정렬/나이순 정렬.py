n = int(input())
ppl = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ppl.append((age,name,i))

result = sorted(ppl, key=lambda x: (x[0],x[2]))

for i in range(n):
    print("{} {}".format(result[i][0], result[i][1]))