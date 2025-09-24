def swap(x, y):
    """
    # Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Error: x and y must be numeric.")
        return -1

    # Swap the values using tuple assignment
    x, y = y, x

    # Print the swapped values
    print(f"Swapped values are numeric: x = {x}, y = {y}")

    return
   
    # Task 2
    # Invoke the function "swap" using the following scenarios:

    # Scenario 1: Non-numeric input
    print("Scenario 1:")
    swap("Apple", 10)

    # Scenario 2: Numeric input
    print("\nScenario 2:")
    swap(9, 17)
