import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.array(X, dtype=float)
    mean = sum(X) / len(X)
    x_c = X - mean

    N = X.shape[0]
    cov = (x_c.T @ x_c) / (N-1)
    
    return cov