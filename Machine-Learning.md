# Machine Learning

```python
X = dataset.iloc[: , :-1].values
y = dataset.iloc[:, -1].values
```

```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy = "mean")
imputer.fit(X[:, 1:3])
X[: , 1:3] = imputer.transform(X[: , 1:3])
```



## 1. Encoding in Machine Learning

Encoding in machine learning refers to the process of converting categorical data into a numerical format that machine learning algorithms can work with. This is important because many machine learning algorithms require numerical input data.

### Example with Binary Encoding (0 and 1)
- Original Data:
  ```
  [['France', 44.0, 72000.0],
   ['Spain', 27.0, 48000.0],
   ...
  ]
  ```
- Binary Encoded Data (One-Hot Encoding):
  ```
  [['1', '0', '0', 44.0, 72000.0],
   ['0', '0', '1', 27.0, 48000.0],
   ...
  ]
  ```

## 2. Feature Encoding and Categorical Values
- Feature encoding refers to the process of converting categorical features (like country names) into a numerical format that machine learning algorithms can process.
- One common method is One-Hot Encoding, where each category is converted into a binary vector.

### Example with One-Hot Encoding
- Original Data:
  ```
  [['France', 44.0, 72000.0],
   ['Spain', 27.0, 48000.0],
   ...
  ]
  ```
- One-Hot Encoded Data:
  ```
  [['1', '0', '0', 44.0, 72000.0],
   ['0', '0', '1', 27.0, 48000.0],
   ...
  ]
  ```

## 3. Using ColumnTransformer in scikit-learn

`ColumnTransformer` in scikit-learn allows for applying different transformations to different columns of a dataset.

### Example with One-Hot Encoding and StandardScaler
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd

# Sample data
data = [['France', 44.0, 72000.0],
        ['Spain', 27.0, 48000.0],
        ['Germany', 30.0, 54000.0],
        ['Spain', 38.0, 61000.0],
        ['Germany', 40.0, 63777.78],
        ['France', 35.0, 58000.0]]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=['Country', 'Age', 'Salary'])

# Define transformers for each type of column
transformers = [('country_encoder', OneHotEncoder(), ['Country']),
                ('scaler', StandardScaler(), ['Age', 'Salary'])]

# Create ColumnTransformer with remainder='passthrough'
ct = ColumnTransformer(transformers, remainder='passthrough')

# Transform the data
X_encoded = ct.fit_transform(df)
```

- `transformers`: List of transformers to be applied to specific columns.
- `remainder='passthrough'`: Keep other columns unchanged.
- Applied One-Hot Encoding to 'Country' and StandardScaler to 'Age' and 'Salary'.

## 4. Step-by-Step Transformation

### Example Data:
```
| Country | Age  | Salary   |
|---------|------|----------|
| France  | 44.0 | 72000.0  |
| Spain   | 27.0 | 48000.0  |
| Germany | 30.0 | 54000.0  |
...
```

### Step-by-Step Transformation using ColumnTransformer
1. Apply One-Hot Encoder to 'Country':
```
| Country | Age  | Salary   | Country_France | Country_Germany | Country_Spain |
|---------|------|----------|----------------|-----------------|---------------|
| France  | 44.0 | 72000.0  | 1              | 0               | 0             |
| Spain   | 27.0 | 48000.0  | 0              | 0               | 1             |
...
```

2. Apply StandardScaler to 'Age' and 'Salary':
```
| Country_France | Country_Germany | Country_Spain | Scaled_Age | Scaled_Salary |
|----------------|-----------------|---------------|------------|---------------|
| 1              | 0               | 0             | 0.862745   | 0.883883      |
| 0              | 0               | 1             | -2.000000  | -1.416860     |
...
```

