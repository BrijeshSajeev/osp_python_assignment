# Multiply all the values in a dictionary.

def multiply_val_in_dict(dictionary):
  result = 1
  for key in dictionary:
    result *= dictionary[key]
  return result

# Example usage
dictionary = {"a": 2, "b": 3, "c": 4}
print(multiply_val_in_dict(dictionary)) # 24
