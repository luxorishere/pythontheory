# Car price to be checked

1. See how much data you have

```python
car.shape
```
2. Find the null and irregular values

```python
car.info()
```
To fill the null value in the column

```python
car["column"].fillna(car["column"].mean(),inplace=True)
```

3. See the uniqueness in data column 

It means isn't there any garbage value other than just relative values

```python
car["column"].unique()
```

Maths for data Science Statistics l <br>
Java OOPs cs l<br>
Tafl cs s<br>
OS s<br>
Web Development s

College Studies 
Tafl
Java
Python

- Python bacics
- Python Tools
- Python Maths &rarr; Statistics, Linear Algebra, Probability, Hypothesis Testing
- Python Web Development
- Python OOPs
- Python Database
- Python Project