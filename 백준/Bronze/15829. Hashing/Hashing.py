import sys

input = sys.stdin.readline

L = int(input().strip())
string = input().strip()

sum=0
for i in range(L):
    sum+=(ord(string[i])-96)*31**i

print(sum)

    
    