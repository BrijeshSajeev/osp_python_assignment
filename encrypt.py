# Print an encrypted message by shifting every small letter in the sentence by -2 position and every capital letter by -3 position. You can assume there are no special characters except spaces and numeric value.

def encrypt_message(message):
  encrypted_message = ""
  for char in message:
    if char.islower():
      encrypted_char = chr((ord(char) - 2 - ord('a')) % 26 + ord('a'))
    elif char.isupper():
      encrypted_char = chr((ord(char) - 3 - ord('A')) % 26 + ord('A'))
    else:
      encrypted_char = char
    encrypted_message += encrypted_char
  print(encrypted_message)

message = "Hello, Everyone!"
encrypt_message(message)
