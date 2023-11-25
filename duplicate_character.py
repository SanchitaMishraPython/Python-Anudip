# Given string with duplicate words
string = "String and String Function"

# Initialize an empty string to store unique words
unique_str = " "

# Split the string into a list of words
split_string = string.split()

# Iterate through each word in the split string
for word in split_string:
    # Check if the word is not already in the unique string
    if word not in unique_str:
        # Concatenate the unique word to the result string
        unique_str = unique_str + " " + word

# Display the original and modified strings
print("The string before removing duplicate:", string)
print("The string after removing duplicate:", unique_str)

#The string before removing duplicate: String and String Function
#The string after removing duplicate:   String and Function


