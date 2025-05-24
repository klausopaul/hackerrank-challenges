import time


def minion_game(string):
    string = string.upper()
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.10f} seconds")


start_time = time.time()
# s = input("Text: ").upper()
with open("input_banana.txt") as f:
    s = f.read().strip().upper()

minion_game(s)
