def string_reverse(s):

# Task 1
# Create a function that reverses a given string (s). - s must be a string.  - Return the reversed string.

    # Check if the input is a string
    if not isinstance(s, str):
        print("Error: The input must be a string.")
        return None

    # Reverse the string using slicing
    reversed_s = s[::-1]

    # Return the reversed string
    return reversed_s

# Task 2
# Invoke the function "string_reverse" using the following scenarios:

# Scenario 1
print("Scenario 1:")
reversed_string1 = string_reverse("Hello World")
print(f"Original string: 'Hello World'")
print(f"Reversed string: '{reversed_string1}'\n")

# Scenario 2
print("Scenario 2:")
reversed_string2 = string_reverse("Python")
print(f"Original string: 'Python'")
print(f"Reversed string: '{reversed_string2}'")
