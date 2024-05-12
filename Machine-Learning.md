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
