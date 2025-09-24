def find_and_replace(lst, find_val, replace_val):
    # Task 1

    # Check if the first argument is a list.
    if not isinstance(lst, list):
        print("Error: The first argument must be a list.")
        return None

    # Iterate through the list and replace values.
    # We use a for loop with range(len(lst)) to get the index.
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Scenario 1
print("Scenario 1:")
list1 = [1, 2, 3, 4, 2, 2]
find1 = 2
replace1 = 5
modified_list1 = find_and_replace(list1, find1, replace1)
print(f"Original List: {list1}")
print(f"Modified List: {modified_list1}")

# Scenario 2
print("\nScenario 2:")
list2 = ["apple", "banana", "apple"]
find2 = "apple"
replace2 = "orange"
modified_list2 = find_and_replace(list2, find2, replace2)
print(f"Original List: {list2}")
print(f"Modified List: {modified_list2}")
