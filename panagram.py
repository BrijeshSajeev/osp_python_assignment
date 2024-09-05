# Given an English sentence, check whether it is a panagram or not. [A panagram is a sentence containing all 26 letters in the English alphabet]
def is_pangram(sentence):
  alphabet = set('abcdefghijklmnopqrstuvwxyz')
  sentence = sentence.lower()
  sentence = sentence.replace(" ", "")
  sentence = set(sentence)
  return sentence == alphabet

# Example usage
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
  print("The sentence is a pangram.")
else:
  print("The sentence is not a pangram.")
