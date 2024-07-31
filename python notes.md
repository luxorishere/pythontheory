## Unit 3

### Python Complex Data Types

1. **Using string data type and string operations**
2. **Defining list and list slicing**
3. **Use of Tuple data type**
4. **String, List, and Dictionary Manipulations**
    - Building blocks of Python programs
    - String manipulation methods
    - List manipulation
    - Dictionary manipulation
5. **Programming using string, list, and dictionary in-built functions**
6. **Python Functions**
7. **Organizing Python codes using functions**

---

### 1. Using String Data Type and String Operations
**Definition:** Strings in Python are sequences of characters. They support various operations like concatenation, repetition, and slicing.

**Code Example:**
```python
s = "Hello"
print(s + " World")  # Concatenation
print(s * 3)         # Repetition
print(s[1:4])        # Slicing
```

**Question:** What will be the output of the above code?

---

### 2. Defining List and List Slicing
**Definition:** Lists are mutable sequences in Python. List slicing allows you to access a subset of list elements.

**Code Example:**
```python
lst = [1, 2, 3, 4, 5]
print(lst[1:3])  # Slicing from index 1 to 2
print(lst[:2])   # Slicing from start to index 1
print(lst[3:])   # Slicing from index 3 to end
```

**Question:** What do the sliced lists contain?

---

### 3. Use of Tuple Data Type
**Definition:** Tuples are immutable sequences in Python, used to store collections of items.

**Code Example:**
```python
t = (1, 2, 3)
print(t[0])  # Accessing elements
```

**Question:** What is the value of `t[0]`?

---

### 4. String, List, and Dictionary Manipulations
#### Building Blocks of Python Programs
**Definition:** Strings, lists, and dictionaries are fundamental data types used in Python programs.

**Code Example:**
```python
# String manipulation
s = "Python"
print(s.upper())

# List manipulation
lst = [1, 2, 3]
lst.append(4)
print(lst)

# Dictionary manipulation
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)
```

**Question:** What are the outputs of the string, list, and dictionary manipulations?

#### String Manipulation Methods
**Definition:** Methods like `upper()`, `lower()`, `replace()`, and `split()` are used to manipulate strings.

**Code Example:**
```python
s = "hello world"
print(s.upper())        # Convert to uppercase
print(s.replace("world", "Python"))  # Replace substring
```

**Question:** What are the outputs of the string manipulation methods?

#### List Manipulation
**Definition:** Lists can be modified using methods like `append()`, `extend()`, `remove()`, and `pop()`.

**Code Example:**
```python
lst = [1, 2, 3]
lst.append(4)    # Add element
lst.remove(2)    # Remove element
print(lst)
```

**Question:** What will `lst` contain after the above manipulations?

#### Dictionary Manipulation
**Definition:** Dictionaries can be modified using methods like `update()`, `pop()`, and `clear()`.

**Code Example:**
```python
d = {"a": 1, "b": 2}
d.update({"c": 3})  # Add new key-value pair
d.pop("a")          # Remove key-value pair
print(d)
```

**Question:** What will `d` contain after the above manipulations?

---

### 5. Programming Using String, List, and Dictionary In-Built Functions
**Definition:** Python provides various in-built functions like `len()`, `sorted()`, `sum()` for strings, lists, and dictionaries.

**Code Example:**
```python
# String length
s = "hello"
print(len(s))

# List sum
lst = [1, 2, 3]
print(sum(lst))

# Dictionary keys
d = {"a": 1, "b": 2}
print(list(d.keys()))
```

**Question:** What are the outputs of the in-built functions for string, list, and dictionary?

---

### 6. Python Functions
**Definition:** Functions are reusable blocks of code that perform a specific task.

**Code Example:**
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

**Question:** What is the output of the `add` function when called with arguments `2` and `3`?

---

### 7. Organizing Python Codes Using Functions
**Definition:** Functions help in organizing code into reusable blocks, making the code more modular and manageable.

**Code Example:**
```python
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("Alice"))
    print(greet("Bob"))

main()
```

**Question:** How does the `main` function help in organizing the code?

---

### Metaphor: Functions as Building Blocks
**Metaphor Explanation:** Think of functions as building blocks in construction. Each function is like a block that serves a specific purpose. By assembling these blocks in different ways, you can build complex structures (programs) efficiently.

**Code Example:**
```python
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def main():
    print(add(2, 3))
    print(multiply(2, 3))

main()
```

**Question:** How does the metaphor of building blocks help you understand the role of functions in Python programs?