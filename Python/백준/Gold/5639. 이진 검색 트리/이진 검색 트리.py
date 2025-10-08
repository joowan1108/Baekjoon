import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

nums = []
while True:
  try:
    n = int(input())
    nums.append(n)
  except ValueError:
    break

def traversal(arr):
  if len(arr) == 0:
    return
  root = arr[0]
  left_arr = []
  right_arr = []
  only_left = True
  for i in range(1, len(arr)):
    if root < arr[i]:
      left_arr = arr[1:i]
      right_arr = arr[i:]
      only_left = False
      break

  if only_left:
    left_arr = arr[1:]
  traversal(left_arr)
  traversal(right_arr)
  print(root)
  
traversal(nums)
    
    
  
  

  

    




  
  

