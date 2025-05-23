def solution(s):
    removed_zeros = 0
    operations = 0
    
    while s!="1":
        removed_zeros += s.count("0")
        s = bin(s.count("1"))[2:]
        operations+=1
        
    return [operations, removed_zeros]
        