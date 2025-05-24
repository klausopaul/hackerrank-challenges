import re
import time
from collections import Counter


def accumulate_points(regex_param):
    total_points = 0
    words_found = []
    regex = re.compile(rf"{regex_param}", re.IGNORECASE)
    for m in regex.finditer((s)):
        p = m.span()[0]
        words_found.extend((s[p]))

        # substrings = [s[p : i + 1] for i in range(p, len(s)) if s[p:i]]
        # words_found.extend(substrings)
        words_found.extend([s[p : i + 1] for i in range(p, len(s)) if s[p:i]])
        # for i in range(p, len(s)):
        #     if s[p:i]:
        #         words_found.append(s[p : i + 1])

    t = Counter((words_found))

    # for k, v in t.items():
    #     total_points += v
    total_points = sum(t.values())

    re.purge()
    return total_points


start_time = time.time()
# s = input("Text: ").upper()
with open("input_banana.txt") as f:
    s = f.read().strip().upper()

Stuart_regex = "[^aeiou]"
Stuart_points = accumulate_points(Stuart_regex)

Kevin_regex = "[aeiou]"
Kevin_points = accumulate_points(Kevin_regex)


if Stuart_points > Kevin_points:
    print(f"Stuart {Stuart_points}")
elif Stuart_points < Kevin_points:
    print(f"Kevin {Kevin_points}")
else:
    print("Draw")

end_time = time.time()
print(f"Execution time: {end_time - start_time:.10f} seconds")
