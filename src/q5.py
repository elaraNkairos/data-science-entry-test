def check_divisibility(num, divisor):
    
    # Task 1
  
    # Check if both inputs are numeric types (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Error: Both num and divisor must be numeric.")
        return False
    
    # Check for division by zero
    if divisor == 0:
        print("Error: Divisor cannot be zero.")
        return False

    # Use the modulo operator to check for divisibility
    # A number is divisible if the remainder of the division is 0
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:

# Scenario 1: Divisible numbers
print("Scenario 1:")
result1 = check_divisibility(10, 2)
print(f"Is 10 divisible by 2? {result1}\n")

# Scenario 2: Non-divisible numbers
print("Scenario 2:")
result2 = check_divisibility(7, 3)
print(f"Is 7 divisible by 3? {result2}\n")

# Extra Scenario for Error Handling:
print("Extra Scenario:")
result3 = check_divisibility(10, "two")
print(f"Is 10 divisible by 'two'? {result3}\n")
