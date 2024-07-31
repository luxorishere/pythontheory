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
