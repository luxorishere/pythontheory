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

```python
# Importing the necessary libraries
import pandas as pd 
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


# Load the dataset
dataset = pd.read_csv("titanic.csv")


# Identify the categorical data
categorical_values = ["Sex", "Embarked", "Pclass"]

# Implement an instance of the ColumnTransformer class


transformers = [("encoder", OneHotEncoder(), categorical_values)]
ct = ColumnTransformer(transformers, remainder = "passthrough")




# Apply the fit_transform method on the instance of ColumnTransformer

X = np.array(ct.fit_transform(dataset))

# Convert the output into a NumPy array



# Use LabelEncoder to encode binary categorical data
le = LabelEncoder()
y = le.fit_transform(dataset["Survived"])


# Print the updated matrix of features and the dependent variable vector
print("Updated Matrix of features:\n", X)
print("Updated dependent variable vector\n",y)

```


### Do we need to apply feature scaling after or before splitting the dataset?

Yes, we need to apply feature scaling after splitting the dataset.

 The reason is: Feature scaling is used to make sure that each feature is on the same scale, so that the algorithms can treat all features equally. If we scale the data before splitting, then we won't be able to tell which features are important just by looking at the scaled data. After splitting the dataset, we can see the distribution of the data in each feature, and we can decide which features to scale based on that.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)
```

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
dataset = pd.read_csv("iris.csv")

# Separate features and target
# Separate features and target
X = dataset.drop('target', axis=1)  # Assuming 'target' is the column name       for the target variable
y = dataset['target']

# Spl
# Split the dataset into an 80-20 training-test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Apply StandardScaler to scale the feature variables
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Print scaled training and test sets
print("Scaled Training Set:")
print(X_train)
print("\nScaled Test Set:")
print(X_test)
```
```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



# Load the Wine Quality Red dataset

dataset = pd.read_csv("winequality-red.csv", delimiter  = ";")
# Separate features and target
X = dataset.drop('quality', axis=1)
y = dataset['quality']



# Split the dataset into an 80-20 training-test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# Create an instance of the StandardScaler class
sc = StandardScaler()


# Fit the StandardScaler on the features from the training set and transform it
X_train = sc.fit_transform(X_train)



# Apply the transform to the test set

X_test = sc.transform(X_test)


# Print the scaled training and test datasets
print(X_train)
print(X_test)
```

## Maths Linear Regression


