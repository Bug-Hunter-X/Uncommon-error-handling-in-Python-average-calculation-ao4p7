def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with an empty list
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#Example usage with a list that contains a non-number
my_list = [1,2,3,'a']
average = calculate_average(my_list)
print(f"The average is: {average}")