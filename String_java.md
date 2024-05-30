# String Operations in Java

## String Class Operations

### Basic Operations
- **Length**: `str.length()`
- **Char At**: `str.charAt(index)`
- **Substring**: `str.substring(beginIndex, endIndex)`
- **Concatenation**: `str1 + str2` or `str1.concat(str2)`
- **Equals**: `str1.equals(str2)`
- **Compare To**: `str1.compareTo(str2)`

### Search Operations
- **Index Of**: `str.indexOf(char)` or `str.indexOf(String)`
- **Last Index Of**: `str.lastIndexOf(char)` or `str.lastIndexOf(String)`
- **Contains**: `str.contains(CharSequence)`

### Case Conversion
- **To Upper Case**: `str.toUpperCase()`
- **To Lower Case**: `str.toLowerCase()`

### Trimming
- **Trim**: `str.trim()`

### Replace
- **Replace**: `str.replace(oldChar, newChar)`
- **Replace All**: `str.replaceAll(regex, replacement)`
- **Replace First**: `str.replaceFirst(regex, replacement)`

### Splitting
- **Split**: `str.split(regex)`

### Other Useful Methods
- **Is Empty**: `str.isEmpty()`
- **Starts With**: `str.startsWith(prefix)`
- **Ends With**: `str.endsWith(suffix)`
- **To Char Array**: `str.toCharArray()`
- **Format**: `String.format(format, args)`

## StringBuilder/StringBuffer Operations

### Basic Operations
- **Append**: `sb.append(String)` or `sb.append(char)`
- **Insert**: `sb.insert(offset, String)`
- **Delete**: `sb.delete(start, end)`
- **Delete Char At**: `sb.deleteCharAt(index)`
- **Replace**: `sb.replace(start, end, String)`
- **Set Char At**: `sb.setCharAt(index, char)`
- **Reverse**: `sb.reverse()`
- **Length**: `sb.length()`
- **Capacity**: `sb.capacity()`
- **Ensure Capacity**: `sb.ensureCapacity(minCapacity)`

### Conversion
- **To String**: `sb.toString()`

## Performance Considerations
- **String**: Immutable, every modification creates a new object.
- **StringBuilder**: Mutable, not synchronized, better for single-threaded scenarios.
- **StringBuffer**: Mutable, synchronized, thread-safe.


## **Java String Methods**

The `String` class in Java offers a rich set of methods for manipulating and working with textual data. These methods can be broadly categorized into the following groups:

**1. Creation and Initialization:**

- `String(char[] value)`: Creates a new `String` object from a character array.
- `String(String anotherString)`: Creates a new `String` object from an existing `String` (useful for defensive copying).
- `String()` (constructor): Creates an empty `String` object.

**2. Basic Operations:**

- `int length()`: Returns the length (number of characters) in the `String`.
- `boolean isEmpty()`: Checks if the `String` is empty (length is 0).
- `char charAt(int index)`: Returns the character at the specified index (0-based).
- `int compareTo(String anotherString)`: Compares this `String` lexicographically with another `String`.
- `boolean equals(Object anotherObject)`: Compares this `String` with another object for equality.
- `boolean equalsIgnoreCase(String anotherString)`: Compares this `String` with another `String` ignoring case.
- `int indexOf(int ch)`: Returns the first index of occurrence of the specified character (or -1 if not found).
- `int indexOf(String str)`: Returns the first index of occurrence of the specified substring (or -1 if not found).
- `int lastIndexOf(int ch)`: Returns the last index of occurrence of the specified character (or -1 if not not found).
- `int lastIndexOf(String str)`: Returns the last index of occurrence of the specified substring (or -1 if not found).
- `String concat(String str)`: Concatenates (joins) this `String` with another `String`.
- `boolean contains(CharSequence s)`: Checks if this `String` contains the specified sequence of characters.
- `boolean startsWith(String prefix)`: Checks if this `String` starts with the specified prefix.
- `boolean endsWith(String suffix)`: Checks if this `String` ends with the specified suffix.

**3. Modification (Creating New Strings):**

- `String substring(int beginIndex, int endIndex)`: Extracts a substring from the beginning index (inclusive) to the end index (exclusive).
- `String replace(char oldChar, char newChar)`: Returns a new `String` where all occurrences of a character are replaced with another character.
- `String replace(CharSequence target, CharSequence replacement)`: Returns a new `String` where all occurrences of a subsequence are replaced with another subsequence.
- `String replaceAll(String regex, String replacement)`: Returns a new `String` where all matches of a regular expression are replaced with a replacement string.
- `String toUpperCase()`: Returns a new `String` with all characters in uppercase.
- `String toLowerCase()`: Returns a new `String` with all characters in lowercase.
- `String trim()`: Returns a new `String` with leading and trailing whitespace removed.
- `String stripLeading(String prefix)`: (JDK 11+) Returns a new `String` with the longest matching leading prefix removed.
- `String stripTrailing(String suffix)`: (JDK 11+) Returns a new `String` with the longest matching trailing suffix removed.

**4. Splitting and Joining:**

- `String[] split(String regex)`: Splits this `String` into an array of substrings based on the given regular expression.
- `String[] split(String regex, int limit)`: Splits this `String` into an array of substrings based on the regular expression, limiting the number of splits.
- `String join(CharSequence delimiter, CharSequence... elements)`: Returns a new `String` by joining elements with a delimiter.

**5. Searching and Matching:**

- `boolean matches(String regex)`: Checks if this `String` matches the given regular expression.

**6. Hashing and Code Generation:**

- `int hashCode()`: Returns a hash code value for this `String`.

**7. Format Specifiers and Conversion:**

- `String format(String format, Object... args)`: Returns a formatted string using the specified format string and arguments.
- `String valueOf(Object obj)`: Returns a string representation of the specified object.

**Additional Notes:**

- Java `String` objects are immutable, meaning that methods that appear to modify the `String` actually create a new `String` object.
- The official Java API documentation provides comprehensive details on each method, including syntax, parameters,