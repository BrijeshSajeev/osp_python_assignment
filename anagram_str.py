# Check whether the given string is an anagram.

def is_anagram(str1, str2):
  if len(str1) != len(str2):
    return False
  return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
# string1 = "arm"
# string2 = "gram"

if is_anagram(string1, string2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")
