import sys

input = sys.stdin.readline

n,m = map(int,input().split())
pokemons = dict()
pokemons_reverse = dict()
for i in range(1,n+1):
	poke = input().strip()
	pokemons[poke]=i
	pokemons_reverse[i]=poke
for _ in range(m):
	q = input().strip()
	if q.isalpha():
		print(pokemons[q])
	else:
		print(pokemons_reverse[int(q)])
		
	
	
        