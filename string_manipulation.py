# In this python script, we will practice string manipulation questions.


# 1. Write a function that processes a list of strings and removes all whitespace, converts each string to lowercase, and returns a list of cleaned strings.

input_string = [
    "  Hello World  ",
    "Python is FUN! ",
    "   CLEAN Code    ",
    "\tWhitespace\tEverywhere\t",
    "LOWERCASE only"]

def sm1(input_string):
    output = []
    for s in input_string:
        #s= "  Hello World  "
        s= s.lower().split()
        output.append("".join(s))
        #print(s)
    return output
    #print("I", input_string)

print(sm1(input_string))


#--------------------------------------------------------------------------------------------------------

# 2. Write a function that takes a list of strings and replaces all numeric characters with #.

input_strings = [
    "User123",
    "Python2024",
    "Version 3.9",
    "100 days of Code",
    "Keep up 7 times"
]

#output = ['User###', 'Python####', 'Version #.#', '### days of Code', 'Keep up # times']

def replace_nu(input_strings):
    output = []
    for word in input_strings:
        result = ""
        for char in word:
            if char.isdigit():
                result+='#'
                #print(result)
            else:
                result+=char
        output.append(result)
    return output
print(replace_nu(input_strings))


#--------------------------------------------------------------------------------------------------------

#3. Write a function that takes a list of strings and returns a new list where each string is reversed and all vowels are removed. Keep the space.

input_strings = [
    "Hello World",
    "Python Programming",
    "Reverse Strings",
    "Vowels are Fun",
    "Keep Learning"
]

# ['dlrW llH', 'gnmmrgrP nhtyP', 'sgnrtS rvsR', 'nF r sllwV', 'gnnrL pK']

def remove_vowel(input_strings):
    
    output =[]
    for word in input_strings:
        # word = "Hello World"
        
        reverse_word = word[::-1]
        
        vowels = "aeiouAEIOU"
        result = ""
        for char in reverse_word:
            if char not in vowels:
                result+=char       
        output.append(result)
    return output

print(remove_vowel(input_strings))

#--------------------------------------------------------------------------------------------------------

#4. Write a function that takes a list of strings, removes punctuation, and converts the string to uppercase.

input_strings = [
    "Hello, World!",
    "Python? Is it fun.",
    "Let's code.",
    "Write clean code.",
    "Practice makes perfect!"
]
# Expected Output: ['HELLO WORLD', 'PYTHON IS IT FUN', 'LETS CODE', 'WRITE CLEAN CODE', 'PRACTICE MAKES PERFECT']
import string
def replace_upper(input_strings):
    output = []
    for word in input_strings:
        # "Hello, World!"
        #print(word)
        result=""
        for char in word:
            if char in string.punctuation: 
                result.replace(char, "")
            else:
                result+=char
        print(result)
        output.append(result.upper())

    return output
print(replace_upper(input_strings))


#--------------------------------------------------------------------------------------------------------------------

# 5. Write a function that takes a list of strings and counts the occurrences of each word in the list, ignoring case.

input_strings = [
    "apple banana apple",
    "Banana Orange Apple",
    "orange APPLE orange",
    "BANANA banana apple"
]
# Expected Output: {'apple': 5, 'banana': 4, 'orange': 3}

def count(input_strings):
    output  = {}
    for string in input_strings:
        #print(string)
        words = string.lower().split(" ")
        for word in words:
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1
        #print(word)

    return output

print(count(input_strings))

#--------------------------------------------------------------------------------------------------------------------

#6. Write a function that takes a string and returns the longest word in the string.
input_string = "I love programming with Python"
#expected output = "programming"

def longest_word(input_string):
    
    words = input_string.split()
    #print(words)

    # Initialize variables for the longest word and its length
    output = ""
    max_length = 0
    
    # Iterate through each word in the list
    for word in words:
        # If the current word is longer than the previous longest, update
        if len(word) > max_length:
            max_length = len(word)
            output = word  # Set the longest word as the current word

    return output
print(longest_word(input_string))