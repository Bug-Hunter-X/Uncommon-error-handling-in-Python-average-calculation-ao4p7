def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

#Example usage with an empty list
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#Example usage with a list that contains a non-number
my_list = [1,2,3,'a']
average = calculate_average(my_list)
print(f"The average is: {average}")

#Example with a list of numbers
my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}") 