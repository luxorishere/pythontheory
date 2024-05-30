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

