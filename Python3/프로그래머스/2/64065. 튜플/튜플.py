from collections import defaultdict

def solution(s):
    s = s[2:len(s)-2]
    s = s.split("},{")
    nums = [list(map(int, st.split(","))) for st in s]
    
    cnt = defaultdict(int) 
    for num in nums:
        for n in num:
            if n in cnt:
                cnt[n]+=1
            else:
                cnt[n]=1
    
    cnt = sorted(cnt, key=lambda x:cnt[x], reverse=True)
    return cnt
    
