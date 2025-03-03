import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def calculate_variance(y):
    return np.var(y)

def knn_regression(X_train, y_train, X_predict, k):
    if k > len(X_train):
        raise ValueError("k must be less than or equal to the number of data points (N).")
    
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)
    
    y_predict = model.predict([[X_predict]])
    return y_predict[0]

def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter k for k-NN regression: "))
    
    X_train = []
    y_train = []
    
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        X_train.append([x])  
        y_train.append(y)
    
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    variance = calculate_variance(y_train)
    print(f"The variance of labels in the training dataset is: {variance}")
    
    X_predict = float(input("Enter the value of X to predict Y: "))
    
    try:
        predicted_y = knn_regression(X_train, y_train, X_predict, k)
        print(f"The predicted value of Y for X = {X_predict} is: {predicted_y}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()