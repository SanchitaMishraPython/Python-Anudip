# Given string
string = "P@#yn26at^&i5ve"

# Initialize counters for alphabets, digits, and special characters
alphabets = digits = special = 0    

# Iterate through each character in the string
for i in range(len(string)):   
    # Check if the character is an alphabet
    if string[i].isalpha():   
        alphabets += 1  
    # Check if the character is a digit
    elif string[i].isdigit():  
        digits += 1     
    # If the character is neither alphabet nor digit, consider it a special character
    else:
        special += 1   
        
# Display the count of alphabets, digits, and special characters
print("\nTotal Number of Alphabets in this String :  ", alphabets)  
print("Total Number of Digits in this String :  ", digits)           
print("Total Number of Special Characters in this String :  ", special)

#Total Number of Alphabets in this String :   8
#Total Number of Digits in this String :   3
#Total Number of Special Characters in this String :   4