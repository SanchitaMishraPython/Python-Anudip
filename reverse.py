def reverse_words(input_string):
    words = input_string.split()
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    reversed_string = ' '.join(reversed_words)
    return reversed_string

input_string = "Deeptech Python Training"
reversed_string = reverse_words(input_string)
print(reversed_string)
