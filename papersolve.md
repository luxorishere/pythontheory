

### Q.3 Attempt any one part of the following

#### (a) Write Python code to sort a sequence of names according to their alphabetical order without using `sort()` function.

```python
def sort_names(names):
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i] > names[j]:
                names[i], names[j] = names[j], names[i]
    return names

# Example usage
names_list = ["John", "Alex", "Zoey", "Christine", "Mike"]
sorted_names = sort_names(names_list)
print("Sorted names:", sorted_names)
```

#### (b) Write a program in Python to create a list of five names by taking input from the user. Now display names in ascending and descending order.

```python
def get_names():
    names = []
    for _ in range(5):
        name = input("Enter a name: ")
        names.append(name)
    return names

def sort_names(names):
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i] > names[j]:
                names[i], names[j] = names[j], names[i]
    return names

# Getting names from the user
names_list = get_names()

# Sorting names
sorted_names = sort_names(names_list.copy())
sorted_names_descending = sorted_names[::-1]

# Displaying names
print("Names in ascending order:", sorted_names)
print("Names in descending order:", sorted_names_descending)
```

### Q.4 Attempt any one part of the following

#### (a) Explain about `seek()` function with a program code in Python.

The `seek()` function is used to change the position of the file handle to a specific location. It takes two parameters: the offset and the reference point. The reference point can be set using `0` (beginning of the file), `1` (current file position), or `2` (end of the file).

Here's a simple example:

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\nThis is the second line.\n")

# Reading from the file and using seek()
with open("example.txt", "r") as file:
    # Move the file handle to the beginning of the file
    file.seek(0)
    print(file.readline())  # Output: Hello, this is a sample file.

    # Move the file handle to the beginning of the second line
    file.seek(len("Hello, this is a sample file.\n"))
    print(file.readline())  # Output: This is the second line.
```

#### (b) What are the different modes used in file handling? Give a single example in Python to explain the working of each mode.

File handling modes in Python include:
- `'r'`: Read (default mode)
- `'w'`: Write (creates a new file or truncates the existing file)
- `'a'`: Append (writes data to the end of the file)
- `'b'`: Binary mode
- `'t'`: Text mode (default mode)
- `'+'`: Read and write

Here are examples demonstrating each mode:

```python
# 'r' mode: Read mode
with open("example.txt", "r") as file:
    content = file.read()
    print("Read mode content:", content)

# 'w' mode: Write mode
with open("write_example.txt", "w") as file:
    file.write("This file is created using write mode.")

# 'a' mode: Append mode
with open("write_example.txt", "a") as file:
    file.write("\nThis line is added using append mode.")

# 'b' mode: Binary mode
with open("example.txt", "rb") as file:
    binary_content = file.read()
    print("Binary mode content:", binary_content)

# 't' mode: Text mode (default mode)
with open("example.txt", "rt") as file:
    text_content = file.read()
    print("Text mode content:", text_content)

# '+' mode: Read and write mode
with open("example_plus.txt", "w+") as file:
    file.write("This file is created using read and write mode.")
    file.seek(0)
    plus_content = file.read()
    print("Read and write mode content:", plus_content)
```

