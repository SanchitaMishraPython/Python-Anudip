def is_armstrong_number(num):
    # Convert the number to a string to find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Test the function with a sample number
sample_number = 153
if is_armstrong_number(sample_number):
    print(f'{sample_number} is an Armstrong number.')
else:
    print(f'{sample_number} is not an Armstrong number.')
#output
#153 is an Armstrong number.