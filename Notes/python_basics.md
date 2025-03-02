

1. what is Python? explain main features?
2. what is difference between mutable vs immuatble
    -   **Mutable types**: Can be modified after creation (e.g., list, dict, set).
    -   **Immutable types**: Cannot be changed after creation (e.g., int, str, tuple).
3. what is difference between list and tuple?
    - List:
        - mutable
        - slower performance than tuple
        - more memory usage than tuple
    - Tuple:
        - Immutable
        - Faster performance than tuple
        - less memory usage than tuple

4. What are Python’s built-in data types?
    -   Numbers: int, float, complex
    -   Sequences: list, tuple, range, str
    -   Set Types: set, frozenset
    -   Mappings: dict
    -   Boolean: bool
    -   Binary: bytes, bytearray, memoryview

5. Explain slicing in Python.
    - Slicing in Python is a technique used to extract a portion of a sequence (like a string, list, or tuple) using a specific syntax. It allows you to retrieve multiple elements by specifying a start index, stop index, and step size.
    -  sequence[start:stop:step]
        - Where:
            -   start → The index to start from (inclusive).
            -   stop → The index to stop at (exclusive).
            -   step → The step size (increment).
    ```
    text = "hello"
    print(text[::])  # Output: "hello"

    text = "hello"
    print(text[1:4])  # Output: "ell"

    text = "abcdef"
    print(text[::2])  # Output: "ace"

    text = "hello"
    print(text[::-1])  # Output: "olleh"

    text = "abcdef"
    print(text[::-2])  # Output: "fdb"

    text = "hello"
    print(text[1:])   # Remove first character → "ello"
    print(text[:-1])  # Remove last character → "hell"
    ```



6. What is type casting in Python?
    -   Converting one data type into another.

7. What is the difference between f = open("log1.txt", "r") and with open("log1.txt", "r") as f:?
    - Difference lies in resource management and how the file is closed.
    - Issues using open() Without with (Manual File Handling) 
        -   Forgetting to close the file → Can lead to memory leaks.
        -   Error Handling → If an exception occurs before f.close(), the file remains open, causing resource leakage
        -   Resource Consumption → Open file handles may exhaust system limits.
    -

8. How does Python handle memory management?
    -   Automatic garbage collection via reference counting and cyclic garbage collector.
    -   gc module can be used to manually manage memory.
    -   Objects are deallocated when no references exist.

9. What are Python decorators?
    -   A decorator is a function that modifies another function’s behavior without modifying its code.
    ```
        def decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper

        @decorator
        def say_hello():
            print("Hello!")

        say_hello()
    ```
    OUTPUT

    ```
    Before function call
    Hello!
    After function call
    ```

10. How does Python implement multithreading?
    -   Python’s GIL prevents true parallel execution of threads.
    -   Use multiprocessing instead for CPU-bound tasks.
    -   Use threading for IO-bound tasks.