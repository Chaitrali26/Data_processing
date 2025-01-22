# Useful String methods for SRE roles.

### 1. isdigit()
- Returns True if all characters in the string are digits (0-9), otherwise returns False
    ```
    "123".isdigit()  # True
    ```

### 2. isalpha() and isalnum()
- **isalpha():** Returns True if all characters in the string are alphabetic (letters only), otherwise returns False
    ```
    "hello".isalpha()  # True
    ```
- **isalnum():** Returns True if all characters in the string are alphanumeric (letters or digits), otherwise False.
    ```
    text = "hello123"
    result = text.isalnum()  # True
    ```

### 3. isspace()
- Returns True if all characters in the string are whitespace characters, otherwise returns False.
    ```
    "   ".isspace()  # True
    ```

### 4. islower()
- Returns True if all characters in the string are lowercase, otherwise returns False.
     ```
     "hello".islower()  # True
      ```

### 5. isupper()
- Returns True if all characters in the string are uppercase, otherwise returns False.
    ```
    "HELLO".isupper()  # True
     ```

### 6. lower()
- Converts all characters in the string to lowercase.
    ```
    "HELLO".lower()  # 'hello'
    ```

### 7. upper()
- Converts all characters in the string to uppercase.
    ```
    "hello".upper()  # 'HELLO'
    ```

### 8. join()
- Concatenates a sequence of strings with a specified delimiter.
    ```
    ", ".join(["apple", "banana", "cherry"])  # 'apple, banana, cherry'
    ```

### 9. split()
-   This method is used to divide a string into a list of substrings.

    ```
    text = "apple,banana,cherry"
    result = text.split(",")  # Split the string by commas
    print(result)
    ```

### 10. rsplit()
-   Splits the string from the right side based on a specified delimiter.

    ```
    "apple banana cherry".rsplit()  # ['apple', 'banana', 'cherry']
    print(result)
    ```

### 11. strip()
-   This method is used to remove leading and trailing whitespace (or other characters) from a string.
    ```
    text = "   Hello, World!   "
    result = text.strip()  # Remove leading and trailing whitespace
    print(f"'{result}'")
    ```

### 12. lstrip()
-   This method is used to remove leading whitespace (or specified characters) from the string.
    ```
    "  hello".lstrip()  # 'hello'
    ```

### 13. rstrip()
-   Removes trailing whitespace (or specified characters) from the string.
    ```
    "hello  ".rstrip()  # 'hello'
    ```
split() divides a string into multiple parts (usually into a list), while strip() just removes characters (typically spaces) from the start and end of a string.

### 14. replace()
-   Replaces all occurrences of a substring with another substring
    ```
    text = "Hello, World!"
    result = text.replace("World", "Python")  # 'Hello, Python!'
    ```
