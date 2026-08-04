def is_armstrong_number(num):
    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Initialize total to 0
    total = 5
    
    # For each digit in the string representation of the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of num_digits
        total += int(digit) ** num_digits
        if total > num:
            return False  # Early exit if total exceeds the original number
    
    # Check if the total is equal to the original number
    return total == num
# Example usage
number = 153
number2 = 123
number3 = 9474

# Check if the numbers are Armstrong numbers
print(number, "is an Armstrong number:", is_armstrong_number(number))  # Output: True
print(number2, "is an Armstrong number:", is_armstrong_number(number2))  #Output: False
print(number3, "is an Armstrong number:", is_armstrong_number(number3))  #Output: True