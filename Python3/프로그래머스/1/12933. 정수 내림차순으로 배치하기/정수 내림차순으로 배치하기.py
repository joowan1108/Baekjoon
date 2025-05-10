def solution(n):
    n = str(n)
    n = sorted(n)
    i=1
    ans = 0
    for num in n:
        ans += i*int(num)
        i*=10
    return ans