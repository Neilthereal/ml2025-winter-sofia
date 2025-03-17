import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def get_data(num_points, dataset_name):
    data = []
    print(f"Enter {num_points} (x, y) pairs for {dataset_name}:")
    for _ in range(num_points):
        x = float(input("Enter x: "))
        y = int(input("Enter y: "))
        data.append((x, y))
    return np.array(data)

def main():
    N = int(input("Number of training points (N): "))
    train_data = get_data(N, "training set")
    X_train, y_train = train_data[:, 0].reshape(-1, 1), train_data[:, 1]
    
    M = int(input("Enter the number of points (M): "))
    test_data = get_data(M, "test set")
    X_test, y_test = test_data[:, 0].reshape(-1, 1), test_data[:, 1]
    
    best_k = 1
    best_accuracy = 0
    
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        if accuracy > best_accuracy:
            best_k = k
            best_accuracy = accuracy
    
    print(f"Best k: {best_k}, Test Accuracy: {best_accuracy:.2f}")

if __name__ == "__main__":
    main()


