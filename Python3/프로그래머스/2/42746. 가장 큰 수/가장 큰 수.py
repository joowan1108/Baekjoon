from functools import cmp_to_key

def comparison(n1, n2):
    str1 = str(n1) + str(n2)
    str2 = str(n2) + str(n1)
    if int(str1) > int(str2):
        return 1
    elif int(str1) < int(str2):
        return -1
    else:
        return 0
    
    

def solution(numbers):
    numbers = sorted(numbers, key=cmp_to_key(lambda x,y : comparison(x,y)), reverse=True)
    
    ans = "".join(str(num) for num in numbers)
    if ans[0]=="0":
        return "0"
    return ans
    