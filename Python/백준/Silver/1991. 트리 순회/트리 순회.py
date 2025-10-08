import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

tree = dict()

for _ in range(n):
  root, right, left = input().rstrip().split()
  tree[root] = [right, left]

def pre_order(k):
  if k!='.':
    print(k, end='')
    pre_order(tree[k][0])
    pre_order(tree[k][1])

def mid_order(k):
  if k!='.':
    mid_order(tree[k][0])
    print(k, end='')
    mid_order(tree[k][1])

def post_order(k):
  if k!='.':
    post_order(tree[k][0])
    post_order(tree[k][1])
    print(k, end='')

pre_order('A')
print()
mid_order('A')
print()
post_order('A')

  
  

  

    




  
  

