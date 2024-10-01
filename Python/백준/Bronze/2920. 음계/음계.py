# Online Python-3 Compiler (Interpreter)
import sys
input = sys.stdin.readline
sounds = list(input().strip().split())
sounds = list(map(int, sounds))

temp1 = sorted(sounds, reverse=True)
temp2 = sorted(sounds)

if(sounds==temp1):
    print("descending")
elif(sounds==temp2):
    print("ascending")
else:
    print("mixed")
    


        
