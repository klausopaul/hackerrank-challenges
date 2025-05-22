import re
from collections import Counter
def minion_game(string):

    def accumulate_points(regex_param):
        total_points = 0
        words_found = []
        regex = re.compile(rf"{regex_param}", re.IGNORECASE)
        for m in regex.finditer((s)):
            p = m.span()[0]
            words_found.append((s[p]))

            for i in range(p, len(s)):
                if s[p:i]:
                    words_found.append(s[p : i + 1])

        t = Counter((words_found))

        for k, v in t.items():
            total_points += v

        re.purge()
        return total_points

    Stuart_regex = "[^aeiou]"
    Stuart_points = accumulate_points(Stuart_regex)

    Kevin_regex = "[aeiou]"
    Kevin_points = accumulate_points(Kevin_regex)

    if Stuart_points > Kevin_points:
        print(f"Stuart {Stuart_points}")
    elif Stuart_points < Kevin_points:
        print(f"Kevin {Kevin_points}")
    else:
        print("Draw")# your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)