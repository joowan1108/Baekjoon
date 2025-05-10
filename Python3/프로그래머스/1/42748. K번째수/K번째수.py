def solution(array, commands):
    ans = []
    for i,j,k in commands:
        new_ = array[i-1:j]
        new_.sort()
        ans.append(new_[k-1])
    return ans