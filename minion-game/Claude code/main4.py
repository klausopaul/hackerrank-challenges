# Original code with detailed analysis comments
def analyze_substring_game(string):
    string = string.upper()  # Convert to uppercase for consistent vowel checking
    vowels = "AEIOU"
    kevin_score = 0  # Kevin scores for substrings starting with vowels
    stuart_score = 0  # Stuart scores for substrings starting with consonants

    # CORE LOGIC ANALYSIS:
    # This loop examines each position in the string as a potential starting point
    for i in range(len(string)):
        if string[i] in vowels:
            # Kevin gets credit for ALL substrings starting at position i
            # Score = remaining characters from position i (including position i itself)
            kevin_score += len(string) - i
        else:
            # Stuart gets credit for ALL substrings starting at position i
            # Score = remaining characters from position i (including position i itself)
            stuart_score += len(string) - i

    # Determine and announce winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

    return kevin_score, stuart_score


# DEMONSTRATION: Let's trace through an example
def demonstrate_with_example():
    test_string = "BANANA"
    print(f"Analyzing string: {test_string}")
    print(f"Length: {len(test_string)}")
    print("\nPosition-by-position breakdown:")

    vowels = "AEIOU"
    kevin_total = 0
    stuart_total = 0

    for i in range(len(test_string)):
        char = test_string[i]
        points = len(test_string) - i
        player = "Kevin (vowel)" if char in vowels else "Stuart (consonant)"

        print(f"Position {i}: '{char}' -> {player} gets {points} points")

        if char in vowels:
            kevin_total += points
        else:
            stuart_total += points

    print(f"\nFinal scores: Kevin={kevin_total}, Stuart={stuart_total}")
    return kevin_total, stuart_total


# What the code ACTUALLY counts (substrings starting at each position):
def show_actual_substrings():
    test_string = "BANANA"
    vowels = "AEIOU"

    print(f"All possible substrings from '{test_string}':")
    print("\nKevin's substrings (starting with vowels):")
    kevin_count = 0
    for i in range(len(test_string)):
        if test_string[i] in vowels:
            for j in range(i + 1, len(test_string) + 1):
                substring = test_string[i:j]
                print(f"  '{substring}' (starts at position {i})")
                kevin_count += 1

    print(f"\nStuart's substrings (starting with consonants):")
    stuart_count = 0
    for i in range(len(test_string)):
        if test_string[i] not in vowels:
            for j in range(i + 1, len(test_string) + 1):
                substring = test_string[i:j]
                print(f"  '{substring}' (starts at position {i})")
                stuart_count += 1

    print(f"\nTotal substring counts: Kevin={kevin_count}, Stuart={stuart_count}")


# COMPARING MATHEMATICAL PATTERNS ACROSS DIFFERENT EXAMPLES
def demonstrate_pattern_consistency():
    """
    This function shows how the mathematical principle applies universally
    across different strings, revealing the underlying pattern
    """
    examples = ["CAR", "OCEAN", "PROGRAMMING"]
    vowels = "AEIOU"

    for example in examples:
        print("=" * 70)
        print(f"ANALYZING: '{example}' (Length: {len(example)})")
        print("=" * 70)

        # First, let's understand the mathematical landscape
        print("Mathematical landscape:")
        for i in range(len(example)):
            possible_substrings = len(example) - i
            print(f"  Position {i}: Can generate {possible_substrings} substrings")
        print()

        # Now trace through the algorithm's logic
        kevin_total = 0
        stuart_total = 0

        print("Step-by-step algorithm execution:")
        for i in range(len(example)):
            char = example[i]
            is_vowel = char in vowels
            player = "Kevin" if is_vowel else "Stuart"
            points_earned = len(example) - i

            print(f"Position {i}: '{char}' ({'vowel' if is_vowel else 'consonant'})")
            print(f"  → {player} earns {points_earned} points")
            print(f"  Substrings generated from this position:")

            # Show the actual substrings to maintain the connection to reality
            for end in range(i + 1, len(example) + 1):
                substring = example[i:end]
                print(f"    '{substring}'")

            if is_vowel:
                kevin_total += points_earned
            else:
                stuart_total += points_earned
            print()

        # Reveal the final pattern
        print(f"Final scores: Kevin = {kevin_total}, Stuart = {stuart_total}")

        # Show the mathematical insight about total points
        total_possible_points = sum(len(example) - i for i in range(len(example)))
        print(f"Total points distributed: {kevin_total + stuart_total}")
        print(f"Mathematical verification: {total_possible_points}")
        print(
            f"✓ Conservation of points verified: {kevin_total + stuart_total == total_possible_points}"
        )

        # Reveal who wins and why
        if kevin_total > stuart_total:
            winner = "Kevin"
            margin = kevin_total - stuart_total
            print(f"Winner: Kevin by {margin} points")
        elif stuart_total > kevin_total:
            winner = "Stuart"
            margin = stuart_total - kevin_total
            print(f"Winner: Stuart by {margin} points")
        else:
            print("Result: Perfect tie!")

        print("\n")


# DEEP DIVE: Understanding why position matters so much
def explore_positional_impact():
    """
    This function reveals why early positions have disproportionate influence
    and how this creates strategic implications
    """
    print("=" * 70)
    print("DEEP DIVE: Why Position Creates Such Dramatic Score Differences")
    print("=" * 70)

    test_string = "AEIOU"  # All vowels for clear demonstration
    print(f"Using '{test_string}' (all vowels - Kevin gets everything)")
    print()

    print("Positional impact analysis:")
    total_score = 0
    for i in range(len(test_string)):
        points_from_position = len(test_string) - i
        percentage_of_total = (
            points_from_position / sum(range(1, len(test_string) + 1))
        ) * 100
        total_score += points_from_position

        print(f"Position {i} ('{test_string[i]}'): {points_from_position} points")
        print(f"  This represents {percentage_of_total:.1f}% of total possible points")
        print(f"  Running total: {total_score}")
        print()

    print(
        f"Key insight: The first character alone contributes {len(test_string)} out of"
    )
    print(
        f"{sum(range(1, len(test_string) + 1))} total points ({(len(test_string)/sum(range(1, len(test_string) + 1)))*100:.1f}%)"
    )
    print()

    print("This explains why strings starting with vowels tend to favor Kevin,")
    print("and strings starting with consonants tend to favor Stuart.")


# PATTERN RECOGNITION EXERCISE
def pattern_recognition_challenge():
    """
    Help the human develop intuition about predicting winners
    """
    print("=" * 70)
    print("PATTERN RECOGNITION: Can you predict the winner?")
    print("=" * 70)

    challenge_strings = ["BEAUTIFUL", "STRENGTH", "EDUCATION"]

    for string in challenge_strings:
        print(f"Challenge: '{string}'")
        print("Before we calculate, try to predict:")
        print("- Which player will win?")
        print("- What makes you think so?")
        print("- How close will the score be?")
        print()

        # Now reveal the answer
        kevin_score = sum(
            len(string) - i for i, char in enumerate(string) if char in "AEIOU"
        )
        stuart_score = sum(
            len(string) - i for i, char in enumerate(string) if char not in "AEIOU"
        )

        print(f"Actual result: Kevin = {kevin_score}, Stuart = {stuart_score}")
        if kevin_score > stuart_score:
            print(f"Kevin wins by {kevin_score - stuart_score} points")
        elif stuart_score > kevin_score:
            print(f"Stuart wins by {stuart_score - kevin_score} points")
        else:
            print("Perfect tie!")

        print("Key factors that determined the outcome:")
        vowel_positions = [i for i, char in enumerate(string) if char in "AEIOU"]
        consonant_positions = [
            i for i, char in enumerate(string) if char not in "AEIOU"
        ]

        if vowel_positions:
            print(f"  Vowels at positions: {vowel_positions}")
            print(
                f"  Average vowel position: {sum(vowel_positions)/len(vowel_positions):.1f}"
            )
        if consonant_positions:
            print(f"  Consonants at positions: {consonant_positions}")
            print(
                f"  Average consonant position: {sum(consonant_positions)/len(consonant_positions):.1f}"
            )

        print("-" * 50)
        print()


# Run all demonstrations
if __name__ == "__main__":
    demonstrate_pattern_consistency()
    explore_positional_impact()
    pattern_recognition_challenge()
