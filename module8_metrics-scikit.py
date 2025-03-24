import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    
    labels
    X = []
    Y = []
    
    for i in range(N):
        x = int(input(f"Enter x (ground truth) for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y (predicted) for point {i+1} (0 or 1): "))
        X.append(x)
        Y.append(y)
    
    X = np.array(X)
    Y = np.array(Y)
    
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()