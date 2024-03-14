import sys

n = int(sys.stdin.readline().rstrip())

a_lst = list(map(int, (sys.stdin.readline().rstrip()).split()))
b_lst = list(map(int, (sys.stdin.readline().rstrip()).split()))

a_lst.sort(reverse=True)
b_lst.sort()
sum=0
for i in range(n):
    sum+=a_lst[i]*b_lst[i]
print(sum)

    




    