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

- Changing the column name: `df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)`
- Creating a new column: `df['new_column'] = some_values`
- Removing a row: `df.drop(index=index_label_to_drop, inplace=True)`
- Removing a column: `del df['column_to_delete']`
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







