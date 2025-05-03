from collections import deque

def solution(n, words):
    prev_words = set()
    stage_num=1
    idx = 0
    while True:
        if idx == len(words):
            break
        for _ in range(n):
            word = words[idx]
            prev_len = len(prev_words)
            prev_words.add(word)
            if prev_len == len(prev_words) or ( idx>0 and word[0]!=prev_word[-1]):
                return [(idx)%n+1, stage_num]
            prev_word = word
            idx+=1
        stage_num+=1
                
    
    return [0,0]
        
        