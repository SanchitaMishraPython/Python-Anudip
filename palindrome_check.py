def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function with a sample string
sample_string = "MALAYALAM"
if is_palindrome(sample_string):
    print(f'"{sample_string}" is a palindrome.')
else:
    print(f'"{sample_string}" is not a palindrome.')
#OUTPUT
#"MALAYALAM" is a palindrome.