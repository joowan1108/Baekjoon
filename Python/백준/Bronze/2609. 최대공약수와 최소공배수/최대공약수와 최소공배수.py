# Online Python-3 Compiler (Interpreter)
import sys
import math
input = sys.stdin.readline

a,b = tuple(map(int, input().strip().split()))

gcd = math.gcd(a,b)
lcm = math.lcm(a,b)

print(gcd)
print(lcm)