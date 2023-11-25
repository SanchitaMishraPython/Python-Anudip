def count_vowels(s):
    # Define the vowels to be counted
    vowels = 'aeiou'
    
    # Convert the input string to lowercase to ensure case-insensitive counting
    s = s.lower()
    
    # Initialize a dictionary to store the count of each vowel
    count = {v: 0 for v in vowels}
    
    # Iterate through each character in the lowercase string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the count for the specific vowel
            count[char] += 1
    
    # Return the final count dictionary
    return count

# Test the function with a sample string
s = "Welcome to python Training"
print(count_vowels(s))

#output
#{'a': 1, 'e': 2, 'i': 2, 'o': 3, 'u': 0}