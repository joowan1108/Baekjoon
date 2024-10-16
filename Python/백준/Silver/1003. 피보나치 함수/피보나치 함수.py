import sys

input = sys.stdin.readline

num_zero = 0
num_one = 0

zeros = [0 for _ in range(0,41)]
ones = [0 for _ in range(0,41)]

zeros[0]=1
ones[1]=1

for i in range(2, len(zeros)):
	zeros[i]=zeros[i-1]+zeros[i-2]
	ones[i]=ones[i-1]+ones[i-2]

	
t = int(input())
for _ in range(t):
	test = int(input())
	print(f"{zeros[test]} {ones[test]}")

		
	
		
	
	
        