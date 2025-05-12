def solution(people, limit):
    people.sort()
    p1 = 0
    p2 = len(people)-1
    boat = 0
    while p1 <= p2:
        if p1==p2:
            boat+=1
            break
        elif people[p1]+people[p2] <= limit:
            p1+=1
            p2-=1
            boat+=1
        elif people[p1]+people[p2] > limit:
            boat+=1
            p2-=1
            
    return boat