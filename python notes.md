## Python Complex Data Types
### Python Complex Data Types
```
   - Using string data type and string operations
   - Defining list and list slicing
   - Use of Tuple data type
   - String, List, and Dictionary Manipulations
   -     Building blocks of Python programs
   -     String manipulation methods
   -     List manipulation
   -     Dictionary manipulation
   - Programming using string, list, and dictionary in-built functions
   - Python Functions
   - Organizing Python codes using functions
   ```
### 1. Using String Data Type and String Operations

**Strings** are sequences of characters enclosed in single quotes ('), double quotes ("), or triple quotes (''' or """).

**Basic Operations:**

* **Concatenation:** Combining strings using the `+` operator.
  ```python
  str1 = "Hello"
  str2 = "World"
  result = str1 + " " + str2
  print(result)  # Output: Hello World
  ```
* **Repetition:** Multiplying a string by an integer repeats it.
  ```python
  str = "Python"
  result = str * 3
  print(result)  # Output: PythonPythonPython
  ```
* **Indexing:** Accessing individual characters using their position (starts from 0).
  ```python
  str = "Python"
  first_char = str[0]
  print(first_char)  # Output: P
  ```
* **Slicing:** Extracting a substring using `[start:end]`.
  ```python
  str = "Python"
  sub_str = str[2:5]
  print(sub_str)  # Output: tho
  ```

**Question:** Given the string "Python Programming", extract the substring "Program".

### 2. Defining Lists and List Slicing

**Lists** are ordered collections of items, enclosed in square brackets `[]`. They can contain elements of different data types.

**Basic Operations:**

* **Accessing elements:** Use indexing to access individual elements.
  ```python
  my_list = [1, 2, "hello", True]
  first_element = my_list[0]
  print(first_element)  # Output: 1
  ```
* **Slicing:** Extract a sublist using `[start:end]`.
  ```python
  my_list = [10, 20, 30, 40, 50]
  sub_list = my_list[1:4]
  print(sub_list)  # Output: [20, 30, 40]
  ```
* **Modifying elements:** Change elements directly using their index.
  ```python
  my_list = [1, 2, 3]
  my_list[0] = 10
  print(my_list)  # Output: [10, 2, 3]
  ```

**Question:** Create a list of fruits, append "orange" to it, and then reverse the list.

### 3. Use of Tuple Data Type

**Tuples** are ordered, immutable collections of items, enclosed in parentheses `()`.

**Basic Operations:**

* **Accessing elements:** Similar to lists, use indexing.
  ```python
  my_tuple = (10, 20, "hello")
  first_element = my_tuple[0]
  print(first_element)  # Output: 10
  ```
* **Unpacking:** Assign elements to multiple variables.
  ```python
  my_tuple = (1, 2, 3)
  a, b, c = my_tuple
  print(a, b, c)  # Output: 1 2 3
  ```

**Question:** Create a tuple of your favorite colors and access the second color.

### 4. String, List, and Dictionary Manipulations

**Building Blocks of Python Programs:**

* **Strings:** Used for text data.
* **Lists:** Used for ordered collections of items.
* **Dictionaries:** Used for unordered key-value pairs.

**String Manipulation Methods:**

* `upper()`: Converts to uppercase.
* `lower()`: Converts to lowercase.
* `strip()`: Removes whitespace from both ends.
* `split()`: Splits a string into a list of substrings.
* `join()`: Joins elements of a list into a string.

**List Manipulation Methods:**

* `append()`: Adds an element to the end.
* `insert()`: Inserts an element at a specific index.
* `remove()`: Removes the first occurrence of an element.
* `pop()`: Removes and returns the last element.
* `sort()`: Sorts the list in ascending order.

**Dictionary Manipulation Methods:**

* `keys()`: Returns a view of the dictionary's keys.
* `values()`: Returns a view of the dictionary's values.
* `items()`: Returns a view of the dictionary's key-value pairs.
* `get()`: Retrieves a value for a given key, with an optional default.
* `update()`: Updates or adds key-value pairs from another dictionary.

**Question:** Create a dictionary of student names and their ages. Add a new student, then retrieve the age of an existing student.

### 5. Programming Using String, List, and Dictionary In-built Functions

**In-built Functions:**

* `len()`: Returns the length of a string, list, or tuple.
* `max()`: Returns the largest item in a list or tuple.
* `min()`: Returns the smallest item in a list or tuple.
* `sorted()`: Returns a sorted list.
* `sum()`: Calculates the sum of numbers in a list.

**Question:** Find the length of a given string, find the maximum number in a list, and calculate the sum of values in a dictionary.

### 6. Python Functions
**Functions** are reusable blocks of code defined using the `def` keyword.

```python
def greet(name):
  print("Hello,", name)

greet("Alice")  # Output: Hello, Alice
```

**Question:** Define a function to calculate the factorial of a number.

### 7. Organizing Python Codes Using Functions

Functions help in code modularity and reusability.

```python
def calculate_area(length, width):
  area = length * width
  return area

def main():
  l = 5
  w = 3
  result = calculate_area(l, w)
  print("Area:", result)

main()
```

**Question:** Create a function to check if a number is prime, and use it in a main function to print all prime numbers up to a given limit.


## Python Complex Data Types Summary

| Data Type | Description | Key Operations |
|---|---|---|
| **String** | Sequence of characters | Concatenation, repetition, indexing, slicing, methods (upper, lower, strip, split, join) |
| **List** | Ordered, mutable collection | Indexing, slicing, modifying elements, methods (append, insert, remove, pop, sort) |
| **Tuple** | Ordered, immutable collection | Indexing, unpacking |
| **Dictionary** | Unordered key-value pairs | Accessing values, adding/removing key-value pairs, methods (keys, values, items, get, update) |

### In-built Functions
| Function | Description |
|---|---|
| `len()` | Returns length |
| `max()` | Returns maximum value |
| `min()` | Returns minimum value |
| `sorted()` | Returns sorted list |
| `sum()` | Calculates sum |

### Functions
* Reusable blocks of code defined using `def` keyword.
* Improve code organization and reusability.

**Example:**
```python
def greet(name):
  print("Hello,", name)
```
## Unit 4 Python File Operations
```
- Python File Operations: Reading files, Writing files in python, Understanding read
functions, read(), readline(), readlines(). 
- Understanding write functions, write() and
writelines() Manipulating file pointer using seek Programming, using file operations. 
```
### Opening Files
The first step to working with a file is to open it. Python provides the `open()` function for this purpose.

```python
file_object = open("filename.txt", "mode")
```
* **filename.txt:** The name of the file you want to open.
* **mode:** Specifies how you want to open the file. Common modes include:
  * `'r'`: Read mode (default)
  * `'w'`: Write mode (creates a new file or overwrites an existing one)
  * `'a'`: Append mode (creates a new file if it doesn't exist, otherwise appends to the end)
  * `'r+'`: Read and write mode
  * `'w+'`: Write and read mode (overwrites existing file)
  * `'a+'`: Append and read mode

### Reading Files
Once a file is opened in read mode, you can read its contents using different methods:

#### `read()`
Reads the entire contents of the file as a string.

```python
file_object = open("data.txt", "r")
content = file_object.read()
print(content)
file_object.close()
```

#### `readline()`
Reads a single line from the file.

```python
file_object = open("data.txt", "r")
line = file_object.readline()
print(line)
file_object.close()
```

#### `readlines()`
Reads all lines of the file and returns them as a list of strings.

```python
file_object = open("data.txt", "r")
lines = file_object.readlines()
for line in lines:
  print(line, end="")
file_object.close()
```

### Writing to Files
To write data to a file, open it in write or append mode.

#### `write()`
Writes a string to the file.

```python
file_object = open("output.txt", "w")
file_object.write("This is some text.")
file_object.close()
```

#### `writelines()`
Writes a list of strings to the file.

```python
file_object = open("output.txt", "a")
lines = ["Line 1\n", "Line 2\n"]
file_object.writelines(lines)
file_object.close()
```

### Manipulating File Pointer
The file pointer indicates the current position within the file. You can use the `seek()` method to move the pointer.

```python
file_object = open("data.txt", "r+")
file_object.seek(10)  # Move pointer to position 10
data = file_object.read(5)  # Read 5 characters from position 10
print(data)
file_object.close()
```

### Closing Files
It's essential to close the file after you're done using it to release system resources.

```python
file_object.close()
```

**Question:**
* How would you read every other line from a text file?

**Compound Question:**
* Write a Python program to copy the contents of one text file to another, converting all text to uppercase in the process.

## Python File Operations Summary

### Opening Files
| Function | Description |
|---|---|
| `open(filename, mode)` | Opens a file with specified mode |
| Modes | `'r'` (read), `'w'` (write), `'a'` (append), `'r+'` (read and write), `'w+'` (write and read), `'a+'` (append and read) |

### Reading Files
| Function | Description |
|---|---|
| `read()` | Reads entire file as a string |
| `readline()` | Reads a single line |
| `readlines()` | Reads all lines into a list |

### Writing to Files
| Function | Description |
|---|---|
| `write(string)` | Writes a string to the file |
| `writelines(list)` | Writes a list of strings to the file |

### File Pointer Manipulation
| Function | Description |
|---|---|
| `seek(offset, whence)` | Moves the file pointer |
| `whence` | 0: start of file, 1: current position, 2: end of file |

### Closing Files
| Function | Description |
|---|---|
| `close()` | Closes the file |

**Remember:**
* Always close files after use to release system resources.
* Use `with` statement for automatic closing (recommended):
  ```python
  with open('file.txt', 'r') as file:
      # Do something with the file
  ```
### File Handling Questions

1. **Change all the vowels in the file to uppercase. Construct a program for the same.**
   - Example:
     - Given a file with the content: `hello world`
     - The result should be: `hEllO wOrld`

2. **Count the number of lines in the file that contain the word 'Python'. Construct a program for the same.**
   - Example:
     - Given a file with the content:
       ```
       I love Python.
       Python is great.
       I enjoy coding.
       ```
     - The result should be: `2`

3. **Reverse the content of each line in the file and save it to a new file. Construct a program for the same.**
   - Example:
     - Given a file with the content:
       ```
       hello
       world
       ```
     - The result should be:
       ```
       olleh
       dlrow
       ```

4. **Remove all the blank lines from the file. Construct a program for the same.**
   - Example:
     - Given a file with the content:
       ```
       hello

       world
       ```
     - The result should be:
       ```
       hello
       world
       ```

5. **Count the frequency of each word in the file. Construct a program for the same.**
   - Example:
     - Given a file with the content: `hello world hello`
     - The result should be: `{'hello': 2, 'world': 1}`

6. **Append the string "End of File" to the end of the file. Construct a program for the same.**
   - Example:
     - Given a file with the content:
       ```
       This is a test file.
       ```
     - The result should be:
       ```
       This is a test file.
       End of File
       ```

7. **Replace all occurrences of a specified word with another word in the file. Construct a program for the same.**
   - Example:
     - Given a file with the content: `I love Python. Python is great.`
     - Replace "Python" with "programming"
     - The result should be: `I love programming. programming is great.`

8. **Copy the contents of one file to another file. Construct a program for the same.**
   - Example:
     - Given a source file with the content: `This is the source file.`
     - The target file should have the content: `This is the source file.`

9. **Count the number of words in the file. Construct a program for the same.**
   - Example:
     - Given a file with the content: `This is a test file.`
     - The result should be: `5`

10. **Extract all the email addresses from the file. Construct a program for the same.**
    - Example:
      - Given a file with the content:
        ```
        Contact us at support@example.com.
        Send your queries to info@example.org.
        ```
      - The result should be: `['support@example.com', 'info@example.org']`

