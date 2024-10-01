# Online Python-3 Compiler (Interpreter)
import sys
input = sys.stdin.readline

abc = [int(input()) for _ in range(3)]
mult = abc[0]*abc[1]*abc[2]
mult = str(mult)

for i in range(10):
    print(mult.count(str(i)))

        
