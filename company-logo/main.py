from collections import Counter

s = sorted(input().lower())
print(s)

c = Counter(s)
print(c)

for i in c.most_common(3):
    print(i[0], i[1])