import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()

i=0
IOI_cnt=0
nums = 0

while i<m-1:
	tmp = s[i:i+3]
	if(tmp=='IOI'):
		i+=2
		IOI_cnt +=1
		if(IOI_cnt==n):
			nums+=1
			IOI_cnt-=1
	else:
		i+=1
		IOI_cnt=0

print(nums)
		