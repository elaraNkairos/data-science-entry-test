def find_first_negative(lst):
   
    # Task 1

    # Initialize an index for the while loop
    i = 0
    # Loop through the list as long as the index is within the list's bounds
    while i < len(lst):
        # Check if the element at the current index is negative
        if lst[i] < 0:
            # If it is, return that number immediately and exit the loop
            return lst[i]
        # Increment the index to move to the next element
        i += 1

    # If the loop finishes without finding a negative number, return "No negatives"
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenarios:

# Scenario 1: A list with negative numbers
print("Scenario 1:")
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"The first negative number is: {result1}\n")

# Scenario 2: A list with no negative numbers
print("Scenario 2:")
result2 = find_first_negative([2, 10, 7, 0])
print(f"The first negative number is: {result2}")
