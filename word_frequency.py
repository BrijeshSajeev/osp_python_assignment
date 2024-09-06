# Display the frequency of words appearing in a string as a dictionary

def word_frequency(s):
    words = s.split()
    return {word: words.count(word) for word in set(words)}

# Sample input
s = "hello hello how are you"

# Sample output
print(word_frequency(s))


