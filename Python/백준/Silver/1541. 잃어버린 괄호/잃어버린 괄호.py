import sys

input = sys.stdin.readline
eq = input().rstrip()
eq = eq.split('-')

first = eq[0].split('+')
first_operand=0
for n in first:
	first_operand+=int(n)


second = eq[1:]
second_operand=0
for s in second:
	s=s.split('+')
	for n in s:
		second_operand+=int(n)
	
print(first_operand-second_operand)

