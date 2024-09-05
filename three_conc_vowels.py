# Accept a string S. Replace the occurrences of 3 consecutive vowels with * .

def replace_three_consecutive_vowels(s):
    vowels = "aeiouAEIOU"
    i = 0
    while i < len(s) - 2:
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            s = s[:i] + '*' + s[i+3:]
        else:
            i += 1
    return s

# Sample input
# s = "Aaahellooo"
s = 'oooonnaaammmiiii'
# Sample output
print(replace_three_consecutive_vowels(s))
