def solution(nums):
    poke_kinds = set(nums)
    choose = len(nums)//2
    if len(poke_kinds) < choose:
        return len(poke_kinds)
    else:
        return choose
