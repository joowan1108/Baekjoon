import sys
from collections import deque

input = sys.stdin.readline

inputs = []
for _ in range(3):
    inputs.append(input().strip())

def getPrint(num):
    if(num%3 ==0 and num%5==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print(num)
        
for put in inputs:
    if(put.isdigit()):
        idx = inputs.index(put)
        result = int(put)+(3-idx)

getPrint(result)

        
        
        
                    
                    
        
    