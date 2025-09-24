def swap(x, y):

    # Task 1
   
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
