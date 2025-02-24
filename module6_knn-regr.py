import numpy as np

def knn_regression(X_train, y_train, X_query, k):
    distances = np.abs(X_train - X_query)
    nearest_indices = np.argsort(distances)[:k]
    return np.mean(y_train[nearest_indices])

def main():
    N = int(input("Enter number of data points (N): "))
    k = int(input("Enter number of neighbors (k): "))
    
    if k > N or N <= 0 or k <= 0:
        print("Invalid input: k must be <= N and both must be positive.")
        return
    
    X_train = np.array([float(input(f"x[{i+1}]: ")) for i in range(N)])
    y_train = np.array([float(input(f"y[{i+1}]: ")) for i in range(N)])
    X_query = float(input("Enter the X value for the prediction: "))
    
    print(f"Predicted Y value: {knn_regression(X_train, y_train, X_query, k):.4f}")

if __name__ == "__main__":
    main()
