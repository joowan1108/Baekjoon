import sys
input = sys.stdin.readline
lst = []
for _ in range(2):
    lst.append(input().rstrip())

s1, s2 = lst[0], lst[1]

len1, len2 = len(s1), len(s2)

dp = [[0]*(len2+1) for _ in range(len1+1)]

string = [['']*(len2+1) for _ in range(len1+1)]

for i in range(len1):
    for j in range(len2):
        if s1[i]==s2[j]:
            dp[i+1][j+1] = dp[i][j]+1
            string[i+1][j+1] = string[i][j] + s1[i]
        else:
            if dp[i+1][j] > dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
                string[i+1][j+1] = string[i+1][j]
            else:
                dp[i+1][j+1] = dp[i][j+1]
                string[i+1][j+1] = string[i][j+1]

if dp[len1][len2]==0:
    print(dp[len1][len2])
else:
    print(dp[len1][len2])
    print(string[len1][len2])
