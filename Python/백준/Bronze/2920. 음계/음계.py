# Online Python-3 Compiler (Interpreter)
import sys
input = sys.stdin.readline


ascend = 0
descend = 0
mixed = 0

sounds = list(input().strip().split())
sounds = list(map(int, sounds))

for i in range(len(sounds)-1):
    if(sounds[i]>sounds[i+1]):
        descend+=1
    elif(sounds[i]<sounds[i+1]):
        ascend+=1

if(ascend==7):
    print("ascending")
elif(descend==7):
    print("descending")
else:
    print("mixed")
    


        
