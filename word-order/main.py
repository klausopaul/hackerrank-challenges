# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

l = list()
s = set()

nroWords = int(input(""))
for i in range(nroWords):
    word = input("")
    l.append(word)
    s.add(word)

c = Counter(l)

print(len(s))
for value in c.values():
    print(value, end=" ")