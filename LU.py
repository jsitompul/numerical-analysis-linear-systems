import numpy as np

def lu_decomposition(A):
    # Get the number of rows
    n = A.shape[0]
    
    # Initialize L and U matrices
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Decomposition into L and U
    for i in range(n):
        # Construct the upper triangular matrix U
        for k in range(i, n):
            try:
                sum = 0
                for j in range(i):
                    sum += (L[i][j] * U[j][k])
                U[i][k] = A[i][k] - sum
            except Exception as e:
                print(f"Error calculating U[{i}][{k}]: {e}")
        
        # Construct the lower triangular matrix L
        for k in range(i, n):
            try:
                if i == k:
                    L[i][i] = 1  # Diagonal as 1
                else:
                    sum = 0
                    for j in range(i):
                        sum += (L[k][j] * U[j][i])
                    L[k][i] = (A[k][i] - sum) / U[i][i]
            except Exception as e:
                print(f"Error calculating L[{k}][{i}]: {e}")

    return L, U

def solve_lu(L, U, b):
    n = len(b)
    
    # Forward substitution to solve L*y = b
    y = np.zeros(n)
    try:
        for i in range(n):
            sum = 0
            for j in range(i):
                sum += L[i][j] * y[j]
            y[i] = b[i] - sum
    except Exception as e:
        print(f"Error during forward substitution: {e}")
    
    # Back substitution to solve U*x = y
    x = np.zeros(n)
    try:
        for i in range(n-1, -1, -1):
            sum = 0
            for j in range(i+1, n):
                sum += U[i][j] * x[j]
            x[i] = (y[i] - sum) / U[i][i]
    except Exception as e:
        print(f"Error during back substitution: {e}")
    
    return x

def solve_linear_system_lu(A, b):
    try:
        L, U = lu_decomposition(A)
        x = solve_lu(L, U, b)
        return x, L, U
    except Exception as e:
        print(f"Error solving the linear system: {e}")
        return None, None, None