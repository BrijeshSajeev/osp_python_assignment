# Check whether the given  key exists in dictionary. Print the value.

def check_key_in_dict(dictionary, key):
  if key in dictionary:
    print(dictionary[key])
  else:
    print("Key not found.")

# Example usage
dictionary = {"name": "John", "age": 30, "city": "New York"}
key = "age"
check_key_in_dict(dictionary, key)

