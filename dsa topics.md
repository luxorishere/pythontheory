## DSA  Topics

1. Frontend Partition
2. Backend Partition
3. DFS 

## DS Topics learned in Project


1. Train_test_split


```python
pricemodel = df.drop(columns = "selling_price")
price_column = df["selling_price"]
```
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(pricemodel, price_column, test_size = 0.2, random_state = 42)
```

train_test_split is used to split the data into training set and testing set.

This is useful when we have to train our model on some data and then test it on some data which is not used during training.

It helps in evaluating the performance of our model on unseen data.

It takes three parameters:

1. Data to be split
2. test_size: it is the ratio of data to be used for testing
3. random_state: It is used to set the random seed.

It returns two values:

1. Training set
2. Testing set

Random seed is a value that is used to generate random numbers. It is a number that is used to initialize the random number generator.

When we set the random state in train_test_split, we are telling the function to use the same sequence of random numbers each time it is run. This is useful when we want to get the same result each time we run our code.

For example, if we have a dataset with 1000 rows and we split it into training and testing sets with a test size of 0.2, then each time we run the code the split will be different. However, if we set the random state to a fixed value, then each time we run the code the split will be the same.

This is useful when we are debugging our code and we want to make sure that the result is the same each time we run it.

The random state is just a number, it can be any number you want, it is up to you to choose a number that is meaningful to your problem.



