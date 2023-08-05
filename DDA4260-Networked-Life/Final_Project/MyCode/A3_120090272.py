# import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import permutation
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor

# import the dataset
Carseats = pd.read_csv("Carseats.csv")
col_dtype = Carseats.dtypes
Carseats = Carseats.to_numpy()
row, col = Carseats.shape
for (i, dtype) in enumerate(col_dtype):
    if dtype == "object":
        Carseats[:,i] = np.unique(Carseats[:,i], return_inverse = True)[1]
    else:
        Carseats[:,i] = Carseats[:,i].astype(dtype)
X, Y = Carseats[:,range(1,col)], Carseats[:,0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

# Decision tree implementation
def DecisionTree(X_train, Y_train, X_test, Y_test, max_depth = None, least_node_size = 1):
    regressor = DecisionTreeRegressor(max_depth= max_depth, min_samples_leaf= least_node_size)
    regressor = regressor.fit(X_train, Y_train)
    t_predict = regressor.predict(X_train)
    t_mse = mean_squared_error(t_predict, Y_train)
    test_predict = regressor.predict(X_test)
    test_mse = mean_squared_error(test_predict, Y_test)
    return test_predict, t_mse, test_mse

# Bagging tree implementation
def BaggingTree(X_train, Y_train, X_test, Y_test, max_depth = None, n_estimators = 10):
    regressor = BaggingRegressor(base_estimator = DecisionTreeRegressor(max_depth = max_depth), n_estimators = n_estimators)
    regressor = regressor.fit(X_train, Y_train)
    t_predict = regressor.predict(X_train)
    t_mse = mean_squared_error(t_predict, Y_train)
    test_predict = regressor.predict(X_test)
    test_mse = mean_squared_error(test_predict, Y_test)
    return test_predict, t_mse, test_mse

# Random forest implementation
def Random_Forest(X_train, Y_train, X_test, Y_test, n_estimators = 100, max_features = "auto"):
    regressor = RandomForestRegressor(n_estimators = n_estimators, max_features=max_features)
    regressor = regressor.fit(X_train, Y_train)
    t_predict = regressor.predict(X_train)
    t_mse = mean_squared_error(t_predict, Y_train)
    test_predict = regressor.predict(X_test)
    test_mse = mean_squared_error(test_predict, Y_test)
    return test_predict, t_mse, test_mse

# Data statistics
df = pd.read_csv('Carseats.csv')
df = pd.DataFrame(df)
plt.figure(figsize=(20, 20))
n = len(df.columns)
for i in range(n):
    if (i!=6 and i!=9 and i!=10):
        plt.subplot(4, 3, i+1)
        A = df.iloc[:, i].values
        plt.hist(A)
        plt.xlabel('values')
        plt.ylabel('times')
        plt.title(df.columns[i])
    else:
        plt.subplot(4, 3, i+1)
        A = pd.DataFrame(df.groupby(df.columns[i]).size())
        plt.bar(x=list(A.index), height=list(A.iloc[:, 0].values))
        plt.xlabel('classes')
        plt.ylabel('times')
        plt.title(df.columns[i])
plt.show()

# Decision Tree
def task_2(depth_range = (3, 10), node_size_range = (1,10)):
    depth_range = np.linspace(*depth_range[:2], int(depth_range[1])-int(depth_range[0]) + 1 if len(depth_range) == 2 else depth_range[-1], dtype = int)
    node_size_range = np.linspace(*node_size_range[:2], int(node_size_range[1])-int(node_size_range[0]) + 1 if len(node_size_range) == 2 else node_size_range[-1], dtype = int)
    train_error = np.zeros((len(depth_range), len(node_size_range)))
    test_error = np.zeros((len(depth_range), len(node_size_range)))
    for i, depth in enumerate(depth_range):
        for j, node_size in enumerate(node_size_range):
            _, train_mse, test_mse = DecisionTree(X_train, Y_train, X_test, Y_test, max_depth = depth, least_node_size = node_size)
            train_error[i, j] = train_mse
            test_error[i, j] = test_mse
    return train_error, test_error

# Bagging Tree
def bag_error(depth_range, tree_num_range):
    depth_range = np.linspace(*depth_range[:2], int(depth_range[1])-int(depth_range[0]) + 1 if len(depth_range) == 2 else int(depth_range[-1]), dtype = int)
    tree_num_range = np.linspace(*tree_num_range[:2], int(tree_num_range[1])-int(tree_num_range[0]) + 1 if len(tree_num_range) == 2 else int(tree_num_range[-1]), dtype = int)
    train_error = np.zeros((len(depth_range), len(tree_num_range)))
    test_error = np.zeros((len(depth_range), len(tree_num_range)))
    for i, depth in enumerate(depth_range):
        for j, tree_num in enumerate(tree_num_range):
            _, train_mse, test_mse = BaggingTree(X_train, Y_train, X_test, Y_test, max_depth = depth, n_estimators = tree_num)
            train_error[i, j] = train_mse
            test_error[i, j] = test_mse
    return train_error, test_error

# Random Forest
def rf_error(tree_num_range, max_feature_range):
    tree_num_range = np.linspace(*tree_num_range[:2], int(tree_num_range[1])-int(tree_num_range[0]) + 1 if len(tree_num_range) == 2 else int(tree_num_range[-1]),  dtype = int)
    max_feature_range = np.linspace(*max_feature_range[:2], int(max_feature_range[1])-int(max_feature_range[0]) + 1 if len(max_feature_range) == 2 else int(max_feature_range[-1]), dtype = int)
    train_error = np.zeros((len(tree_num_range), len(max_feature_range)))
    test_error = np.zeros((len(tree_num_range), len(max_feature_range)))
    for i, tree_num in enumerate(tree_num_range):
        for j, max_feature in enumerate(max_feature_range):
            _, train_mse, test_mse = Random_Forest(X_train, Y_train, X_test, Y_test, n_estimators = tree_num, max_features = max_feature)
            train_error[i, j] = train_mse
            test_error[i, j] = test_mse
    return train_error, test_error

def Random_Forest_bias_var(X_train, Y_train, X_test, Y_test, tree_num, split_num = 10):
    X_train_split = np.array_split(X_train, split_num)
    Y_train_split = np.array_split(Y_train, split_num)
    prediction = []
    for i in range(split_num):
        regressor = RandomForestRegressor(n_estimators = tree_num, max_depth = 5, max_features = 5)
        regressor = regressor.fit(X_train_split[i], Y_train_split[i])
        prediction.append(regressor.predict(X_test))
    prediction = np.array(prediction)
    test_data_num = X_test.shape[0]
    bias_square = mean_squared_error(sum(prediction)/split_num, Y_test)
    variance = np.trace(np.cov(prediction.T))/test_data_num
    return bias_square, variance

# Bias analysis
def Bias(X_train, Y_train, X_test, Y_test, tree_num_range, forest_num, iter_num = 10):
    num = int(tree_num_range[1])-int(tree_num_range[0])+1 if len(tree_num_range) == 2 else int(tree_num_range[-1])
    bias_square = np.zeros(num)
    variance = np.zeros(num)
    for _ in range(iter_num):
        bias_square_ = []
        variance_ = []
        shuffler = permutation(X_train.shape[0])
        X_train = X_train[shuffler, :]
        Y_train = Y_train[shuffler]
        for tree_num in np.linspace(*tree_num_range[:2], num, dtype = int):
            RF_bias_square, RF_variance = Random_Forest_bias_var(X_train, Y_train, X_test, Y_test, tree_num = tree_num, split_num = forest_num)
            bias_square_.append(RF_bias_square)
            variance_.append(RF_variance) 
        bias_square = bias_square + np.array(bias_square_)
        variance = variance + np.array(variance_)
    bias_square = bias_square/iter_num
    variance = variance/iter_num
    return bias_square, variance
