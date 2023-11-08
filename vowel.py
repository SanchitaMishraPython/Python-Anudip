
def count_vowels(s):
    vowels = 'aeiou'  
    s = s.lower()     
    count = {v: 0 for v in vowels}  
    for char in s:  
        if char in vowels:  
            count[char] += 1  
    return count  

s = "Welcome to python Training"
print(count_vowels(s)) 
