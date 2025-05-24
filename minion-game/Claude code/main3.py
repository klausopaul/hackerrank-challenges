# Original code with detailed analysis comments
def analyze_substring_game(string):
    string = string.upper()  # Convert to uppercase for consistent vowel checking
    vowels = "AEIOU"
    kevin_score = 0   # Kevin scores for substrings starting with vowels
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
            for j in range(i+1, len(test_string)+1):
                substring = test_string[i:j]
                print(f"  '{substring}' (starts at position {i})")
                kevin_count += 1
    
    print(f"\nStuart's substrings (starting with consonants):")
    stuart_count = 0
    for i in range(len(test_string)):
        if test_string[i] not in vowels:
            for j in range(i+1, len(test_string)+1):
                substring = test_string[i:j]
                print(f"  '{substring}' (starts at position {i})")
                stuart_count += 1
    
    print(f"\nTotal substring counts: Kevin={kevin_count}, Stuart={stuart_count}")

# STEP-BY-STEP MATHEMATICAL RELATIONSHIP DEMONSTRATION
def trace_mathematical_relationship():
    """
    This function demonstrates the deep mathematical relationship between
    position-based scoring and actual substring counting
    """
    test_string = "HELLO"
    vowels = "AEIOU"
    
    print("="*60)
    print("TRACING THE MATHEMATICAL RELATIONSHIP")
    print("="*60)
    print(f"String: '{test_string}' (length = {len(test_string)})")
    print()
    
    # Let's trace each position and show both the math and the reality
    total_kevin = 0
    total_stuart = 0
    
    for i in range(len(test_string)):
        char = test_string[i]
        is_vowel = char in vowels
        player = "Kevin" if is_vowel else "Stuart"
        
        # The mathematical prediction: how many substrings start here?
        predicted_substrings = len(test_string) - i
        
        print(f"Position {i}: Character '{char}' ({'vowel' if is_vowel else 'consonant'})")
        print(f"  Mathematical prediction: {predicted_substrings} substrings can start here")
        print(f"  Let's verify by listing them:")
        
        # Now let's actually generate and count the substrings to verify
        actual_substrings = []
        for end in range(i + 1, len(test_string) + 1):
            substring = test_string[i:end]
            actual_substrings.append(substring)
            print(f"    '{substring}'")
        
        actual_count = len(actual_substrings)
        print(f"  Actual count: {actual_count} substrings")
        print(f"  ✓ Prediction matches reality: {predicted_substrings == actual_count}")
        print(f"  → {player} gets {predicted_substrings} points")
        print()
        
        if is_vowel:
            total_kevin += predicted_substrings
        else:
            total_stuart += predicted_substrings
    
    print("="*60)
    print("FINAL VERIFICATION")
    print("="*60)
    print(f"Kevin's total score: {total_kevin}")
    print(f"Stuart's total score: {total_stuart}")
    
    # Now let's verify this matches our original algorithm
    print("\nRunning original algorithm:")
    string_upper = test_string.upper()
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(string_upper)):
        if string_upper[i] in vowels:
            kevin_score += len(string_upper) - i
        else:
            stuart_score += len(string_upper) - i
    
    print(f"Original algorithm results: Kevin={kevin_score}, Stuart={stuart_score}")
    print(f"✓ Results match: {kevin_score == total_kevin and stuart_score == total_stuart}")

# Run the comprehensive demonstration
if __name__ == "__main__":
    trace_mathematical_relationship()