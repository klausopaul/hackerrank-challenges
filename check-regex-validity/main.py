# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
listRegExs = []
if T > 0 and T < 100:
    for i in range (T):
        regEx = input()
        listRegExs.append(regEx)

for e in listRegExs:
    try: 
        re.compile(repr(e))
        print ("True")
    except re.error:
        print ("False")
