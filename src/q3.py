def update_dictionary(dct, key, value):

# Task 1

    # Check if the key already exists in the dictionary.
    if key in dct:
        # If the key exists, print the original value.
        print(f"Key '{key}' already exists. Original value: {dct[key]}")

    # Update the dictionary with the new key-value pair.
    dct[key] = value

    # Return the modified dictionary.
    return dct
    
# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# Scenario 1: Key does not exist
print("Scenario 1:")
dict1 = {}
updated_dict1 = update_dictionary(dict1, "name", "Alice")
print(f"Updated dictionary: {updated_dict1}\n")

# Scenario 2: Key already exists
print("Scenario 2:")
dict2 = {"age": 25}
updated_dict2 = update_dictionary(dict2, "age", 26)
print(f"Updated dictionary: {updated_dict2}")
