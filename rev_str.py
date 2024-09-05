# Reverse the characters in a sentence while keeping the words in their original order 
def reverse_sentence(sentence):
  words = sentence.split()
  reversed_words = [word[::-1] for word in words]
  reversed_sentence = ' '.join(reversed_words)
  return reversed_sentence

# Example usage
sentence = "Hello world, how are you?"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
