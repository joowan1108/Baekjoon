from collections import Counter
import sys
n = int(sys.stdin.readline())
num_lst = []
for _ in range(n):
    num_lst.append(int(sys.stdin.readline()))
summ = sum(num_lst)

avg = round(summ/n)

num_lst.sort()
mid = num_lst[n//2]

count_lst = Counter(num_lst)
count_lst = dict(sorted(count_lst.items(), key=lambda x: (-x[1], x[0])))
keys_lst = list(count_lst.keys())

if(len(keys_lst)>1):
    if(count_lst[keys_lst[0]] == count_lst[keys_lst[1]]):
        most_freq = keys_lst[1]
    else:
        most_freq = keys_lst[0]
else:
    most_freq = keys_lst[0]
    
rangee = max(num_lst) - min(num_lst)

print(avg)
print(mid)
print(most_freq)
print(rangee)


    