from collections import defaultdict
def solution(genres, plays):
    most_genres = dict()
    for i in range(len(genres)):
        if genres[i] in most_genres:
            most_genres[genres[i]] += plays[i]
        else:
            most_genres[genres[i]] = plays[i]
    
    most_genres = sorted(most_genres.items(), key=lambda x: x[1], reverse=True)
    
    tmp = defaultdict(list)
    for i in range(len(genres)):
        if genres[i] in tmp:
            tmp[genres[i]].append((i, plays[i]))
        else:
            tmp[genres[i]] = [(i, plays[i])]

    ans = [] 
    for most in most_genres:
        if len(tmp[most[0]])>=2:
            tmp[most[0]] = sorted(tmp[most[0]], key=lambda x: x[1], reverse=True)
            ans.append(tmp[most[0]][0][0])
            ans.append(tmp[most[0]][1][0])
             
        else:
            ans.append(tmp[most[0]][0][0])
    return ans
    
    
    