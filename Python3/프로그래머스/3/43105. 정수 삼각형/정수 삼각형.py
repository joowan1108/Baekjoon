def solution(triangle):
    n = len(triangle)
    dp = [[0]*len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    if n==1:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]   
    if n==2:
        return max(dp[1])
    for i in range(1, len(triangle)-1):
        for j in range(1, len(triangle[i])):
            dp[i+1][j] = max(dp[i][j-1], dp[i][j]) + triangle[i+1][j]
    
    return max(dp[n-1])
        
            
            