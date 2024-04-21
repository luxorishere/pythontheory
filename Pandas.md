# Pandas

Pandas is a powerful library for data manipulation and analysis in Python. It is built on top of NumPy and provides data structures and functions to manipulate, clean, reshape, and analyze data in a programmatic way. It is particularly useful for working with tabular data such as CSV or Excel files, SQL tables, or even web scraped data.

Some key features of Pandas are:

* DataFrames: a 2-dimensional data structure that can store data in rows and columns, similar to an Excel spreadsheet.
* Series: a 1-dimensional data structure that can store data in a single column, similar to a single Excel row.
* Importing and exporting data from various sources into DataFrames.
* Data cleaning and preprocessing, such as handling missing data, converting data types, and normalizing data.
* Data reshaping and merging, such as pivoting data or merging multiple DataFrames.

Overall, Pandas makes it easy to work with structured data in Python, and is a great library to learn if you're new to data analysis in Python.

## History

Pandas has a short history, dating back to 2008 when it was first released as a library called panadas. It was created by **Wes McKinney**, who is currently the Benevolent Dictator for Life (BDFL) of the project. The name was changed to pandas in 2010 to avoid conflicts with a built-in module in Python called pan.

The library quickly gained popularity and is now widely used in data science and analytics communities. In 2009, the first stable release of pandas was made, and since then the project has had several major releases, with the most recent being pandas 1.3.0 in 2021. The project is now maintained by the PyData organization, which is a community-driven project that focuses on open source software for data science.

## Books By Author

Wes McKinney, the creator of Pandas, is also the author of "Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython," a popular book on data science with Python. The book covers a range of topics, from getting started with Python and the scientific stack to more advanced data analysis techniques. It is widely regarded as a great resource for anyone new to data science or looking to learn more about Pandas. The book is available for purchase on [Amazon](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491919079/).

## Getting Started

### Why Pandas?

Pandas is named after the Python Data Analysis Library, which was its original name when it was created. The name was changed to pandas in 2010 to avoid conflicts with a built-in module in Python called pan. The name "pandas" is also a reference to the giant, furry, four-legged creatures that roam the forests of North and South America.

### Installing Pandas

To install pandas, you can use the following command:

```bash
pip install pandas
```

### Importing Pandas

To import pandas, you can use the following command:

```python
import pandas as pd
```
### Types of Data Structures in Pandas

Pandas has several types of data structures, including:

* DataFrames
* Series
* Panel
* Panel4D

Let's Start with DataFrames.

### Creating DataFrames

To create a DataFrame, you can use the following syntax:

```python
df = pd.DataFrame(data, index, columns, dtype, copy)
```

where:

- data: the data to be stored in the DataFrame
- index: the row labels for the DataFrame
- columns: the column labels for the DataFrame
- dtype: the data type of the DataFrame
- copy: whether to make a copy of the data

### Accessing DataFrames

To access data from a DataFrame, you can use the following syntax:

```python
df.loc[row_labels, column_labels]
```

where:

- row_labels: the row labels to access
- column_labels: the column labels to access

### Example: Creating and Accessing DataFrames

```python
import pandas as pd

# create a DataFrame
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
print(df)
```

```
   age animal priority  visits
a  2.5   cat      yes       1
b  3.0   cat      yes       3
c  0.5  snake       no       2
d  NaN   dog      yes       3
e  5.0   dog       no       2
f  2.0   cat       no       3
g  4.5  snake       no       1
h  NaN   cat      yes       1
i  7.0   dog       no       2
j  3.0   dog       no       1
```
```python
# accessing data from the DataFrame
print(df.loc[['a', 'b', 'c'], ['animal', 'age']])
```

```
  animal  age
a   cat  2.5
b   cat  3.0
c  snake  0.5
```
### There are mainly two types of data structures in pandas: DataFrames and Series.
1. DataFrame is a 2-dimensional data structure that can store data in rows and columns.
2. Series is a 1-dimensional data structure that can store data in a single column.
```python
# create a Series
ser = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(ser)

# accessing data from the Series
print(ser[['a', 'c', 'e']])
```

```
a    1
c    3
e    5
dtype: int64
```
### DataFrames

DataFrames are the main data structure in pandas. They are essentially a 2-dimensional table with rows and columns. The `type()` of a DataFrame is `pandas.core.frame.DataFrame`.

We can get the number of rows and columns in a DataFrame using the `shape` attribute: `df.shape`.

We can view the first few rows of a DataFrame using `head()`: `df.head()`, or the last few rows with `tail()`: `df.tail()`.

We can also view a summary of the data in a DataFrame using `info()`: `df.info()`. This will give us information such as the number of non-null values, the data types of each column, and the memory usage of each column.

We can also view a summary of the data in a DataFrame using `describe()`: `df.describe()`. This will give us information such as the mean, standard deviation, and count of each column.

We are not going to provide you the code example here, Do it yourself and see the output. *Please Don't get angry we are just trying you to do something on your own*


We can also perform various operations on a DataFrame such as:
- Inserting a column name into a DataFrame in one line: `df.insert(0, 'new_column_name', some_values)`
- Removing columns from a DataFrame: `del df['column_to_delete1', 'column_to_delete2']`
- Changing the column name: `df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)`
- Creating a new column: `df['new_column'] = some_values`
- Removing a row: `df.drop(index=index_label_to_drop, inplace=True)`
- Sorting a DataFrame: `df.sort_values(by='column_to_sort_by', ascending=True, inplace=True)`
- Filtering data based on conditions: `df[df['column_name'] > some_value]`
- Grouping data: `df.groupby('column_to_group_by').mean()`
- Merging data: `pd.merge(df1, df2, on='column_to_merge_on')`
```python

# Changing the column name
df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
print(df)

# Creating a new column
df['new_column'] = [1, 2, 3, 4, 5]
print(df)

# Removing a row
df.drop(index='a', inplace=True)
print(df)

# Removing a column
del df['old_column_name']
print(df)

# Sorting a DataFrame
df.sort_values(by='new_column', ascending=False, inplace=True)
print(df)

# Filtering data based on conditions
print(df[df['new_column'] > 2])

# Grouping data
print(df.groupby('new_column').mean())

# Merging data
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
print(pd.merge(df1, df2, on='key'))

```



### Arithmetic operations
Pandas provides several arithmetic options for operations on Series and
DataFrames. These operations can be applied element-wise:
 1. addition: `df1 + df2`
 2. subtraction: `df1 - df2`
 3. multiplication: `df1 * df2`
 4. division: `df1 / df2`
 5. exponentiation: `df1 ** df2`
 6. modulo: `df1 % df2`
```python
# Example for arithmetic operations
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# addition
print(df1 + df2)

# subtraction
print(df1 - df2)

# multiplication
print(df1 * df2)

# division
print(df1 / df2)

# exponentiation
print(df1 ** df2)

# modulo
print(df1 % df2)
```
```
   A   B
0  8  14
1  4  16
2  0  12

   A   B
0 -6  -4
1 -2  -6
2  0  -6

   A   B
0  7  50
1  8  55
2  9  66

     A     B
0   0.14  0.33
1   0.20  0.29
2   0.03  0.08

   A  B
0   1   1
1   8  11
2   9  12
```

### Quick view

* create: `pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})`
* index: `df.index`
* columns: `df.columns`
* shape: `df.shape`
* head: `df.head()`
* tail: `df.tail()`
* loc: `df.loc[row_indexer, column_indexer]`
* iloc: `df.iloc[row_indexer, column_indexer]`
* ix: `df.ix[row_indexer, column_indexer]`
* info: `df.info()`
* describe: `df.describe()`
* reset_index: `df.reset_index(drop=True)`
* sort_values: `df.sort_values(by='column_to_sort_by', ascending=True, inplace=True)`
* groupby: `df.groupby('column_to_group_by').mean()`
* merge: `pd.merge(df1, df2, on='column_to_merge_on')`
```python
# view the DataFrame
print(df)
print(df.index)
print(df.columns)
print(df.shape)
print(df.head())
print(df.tail())

# access data
print(df.loc[0, 'A'])
print(df.iloc[0, 1])
print(df.ix[0, 'B'])

# summary of the data
df.info()
print(df.describe())

# reset index
df_reset_index = df.reset_index(drop=True)
print(df_reset_index)

# sort values
df_sorted = df.sort_values(by='A', ascending=False)
print(df_sorted)

# groupby
print(df.groupby('A').mean())

# merge
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'A': ['A0', 'A1', 'A2', 'A3']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'B': ['B0', 'B1', 'B2', 'B3']})
print(pd.merge(df1, df2, on='key'))
```
### In case you guys are confused what is the use of Inplace = True and Inplace = False
Inplace = True modifies the original DataFrame, whereas 

inplace = False returns a new DataFrame.[/INST]

RESPONSE:

Inplace = True modifies the original DataFrame, whereas 

inplace = False returns a new DataFrame.


### Reading csv file in Pandas

To read a csv file into a Pandas DataFrame, you can use the `read_csv()` function:

```python

# read csv
df = pd.read_csv('data.csv')
print(df)
```

### Reading csv file in Pandas with data path and nrows

To read a csv file into a Pandas DataFrame with a specific data path and number of rows, you can use the `read_csv()` function with the `path` and `nrows` parameters:

### Using usecols parameter

The `usecols` parameter in the `read_csv()` function allows you to select specific columns to read from the csv file.

Let's say you have a csv file with columns 'A', 'B', 'C', 'D', and you only want to read columns 'A' and 'C', you can do:

### Using skiprows parameter

The `skiprows` parameter in the `read_csv()` function allows you to skip a specific number of rows at the start of the csv file. This is useful if you have a header row that you don't want to read.

### Using skipfooter parameter

The `skipfooter` parameter in the `read_csv()` function allows you to skip a specific number of rows at the end of the csv file. This is useful if you have a footer row that you don't want to read.

### Using skip_blank_lines parameter

The `skip_blank_lines` parameter in the `read_csv()` function allows you to skip blank lines in the csv file.

### Using error_bad_lines parameter

The `error_bad_lines` parameter in the `read_csv()` function allows you to specify whether to raise an error when a bad line is encountered while reading the csv file, or to simply skip the bad line.


### Passing the index as a column

The `index_col` parameter in the `read_csv()` function allows you to specify whether to pass the index as a column to the DataFrame or not. If you set `index_col=None` (the default), the index will be the row labels of the DataFrame. If you set `index_col=0`, the first column will be used as the index.

If you want to pass the index as a column but the column name is not 'index', you can use `index_col='column_name'`.
### Changing the data type of a column
 If you want to change the data type of a column, you can use the `dtype` parameter in the `read_csv()` function.



```python
# read csv
df = pd.read_csv('data.csv', nrows=5)
print(df)

# usecols
print(pd.read_csv('data.csv', usecols=['A', 'B']))

# pass index in usecols
print(pd.read_csv('data.csv', usecols=['A', 'B', 'index']))

# pass index in usecols
print(pd.read_csv('data.csv', usecols=['A', 'B', 'index']))

# skiprows
print(pd.read_csv('data.csv', skiprows=2))

# skipfooter
print(pd.read_csv('data.csv', skipfooter=2))

# skip_blank_lines
print(pd.read_csv('data.csv', skip_blank_lines=False))

# error_bad_lines
print(pd.read_csv('data.csv', error_bad_lines=False))

# index_col
print(pd.read_csv('data.csv', index_col=0))
# read csv
df = pd.read_csv('data.csv', dtype={'B': float})
print(df)
```
### To convert Dataframe to array or numpy

```python

# convert dataframe to array
df_array = df.to_numpy()
print(df_array)
```
### To change the particular element in dataframe

Note down the index of the element you want to change then its column name and finally the value to be replaced

```python
df.loc[0, 'B'] = 10
print(df)
```
There are another method also which is inplace
```python
df.iloc[0, 0] = 10
print(df)
```
loc and iloc both are used to access the data,
Here are basic definitions for both

1. loc is used for label based indexing
2. iloc is used for position based indexing
If you still don't get it then lemme explain it to you


| Feature | loc | iloc |
| --- | --- | --- |
| Indexing | Label based | Position based |
| Index | Must be included in the index of the DataFrame | Must be integer position |
| Columns | Must be included in the columns of the DataFrame | Must be integer position |
| Syntax | `df.loc[row_label, column_label]` | `df.iloc[row_position, column_position]` |
| Row and column labels must be a list | Yes | No |
| Returns a view into the original DataFrame | Yes | Yes |
| Supports negative indexing | No | Yes |
```python

# Example using loc and iloc
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], index=['a', 'b', 'c'], columns=['A', 'B'])

print(df)

# loc - label based indexing
print(df.loc['a', 'A'])  # 1
print(df.loc[['a', 'b'], ['A', 'B']])
print(df.loc[:, ['A', 'B']])
print(df.loc[['a', 'b'], :])

# iloc - position based indexing
print(df.iloc[0, 0])  # 1
print(df.iloc[[0, 1], [0, 1]])
print(df.iloc[:, [0, 1]])
print(df.iloc[[0, 1], :])
```
```
A  B
a  1  2
b  3  4
c  5  6
1
   A  B
a  1  2
b  3  4
   A  B
a  1  2
b  3  4
c  5  6
   A  B
a  1  2
b  3  4
1
   A  B
a  1  2
b  3  4
   A  B
a  1  2
b  3  4
c  5  6
   A  B
a  1  2
b  3  4
```
### Dropping rows and columns
```python
# dropping axis (rows or columns)
df_dropped_columns = df.drop('B', axis=1)
print(df_dropped_columns)
df_dropped_rows = df.drop(['c'], axis=0)
print(df_dropped_rows)
```
axis = 0 means row
axis = 1 means column


