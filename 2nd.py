def word_break(n, s, dictionary):
    # Convert the dictionary into a set for faster lookup
    word_set = set(dictionary)
    
    # Initialize the DP array with False values
    dp = [False] * (len(s) + 1)
    
    # Empty string can always be segmented
    dp[0] = True
    
    # Fill the DP array
    for i in range(1, len(s) + 1):
        for j in range(i):
            # If substring s[j:i] is in dictionary and dp[j] is True
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    # Return 1 if the whole string can be segmented, else 0
    return 1 if dp[len(s)] else 0

# Example usage:
n = 6
s1 = "ilike"
dictionary1 = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(word_break(n, s1, dictionary1))  # Output: 1

s2 = "ilikesamsung"
dictionary2 = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(word_break(n, s2, dictionary2))  # Output: 1
