def solution(n, words):
    prev_words = set()
    prev_char = words[0][0]
    
    for i, word in enumerate(words):
        if word in prev_words or word[0]!=prev_char:
            return [(i%n)+1, (i//n)+1]
        else:
            prev_char = word[-1]
            prev_words.add(word)       
    
    return [0,0]
        
        