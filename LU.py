import numpy as np

def lu_decomposition(A):
    # Get the number of rows in matrix A
    n = A.shape[0]
    
    # Initialize L and U matrices with zeros
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Decomposition into L and U matrices
    for i in range(n):
        # Construct the upper triangular matrix U
        for k in range(i, n):
            try:
                # Initialize sum to accumulate the summation for U[i,k]
                sum = 0
                # Calculate the summation of L[i,j] * U[j,k]
                for j in range(i):
                    sum += (L[i,j] * U[j,k])
                # Calculate the value for U[i,k]
                U[i,k] = A[i,k] - sum
            except Exception as e:
                # Catch and print any error during the calculation of U[i][k]
                print(f"Error calculating U[{i},{k}]: {e}")
        
        # Construct the lower triangular matrix L
        for k in range(i, n):
            try:
                if i == k:
                    # Diagonal elements of L are set to 1
                    L[i,i] = 1
                else:
                    # Initialize sum to accumulate the summation for L[k,i]
                    sum = 0
                    # Calculate the summation of L[k,j] * U[j,i]
                    for j in range(i):
                        sum += (L[k,j] * U[j,i])
                    # Calculate the value for L[k,i]
                    L[k,i] = (A[k,i] - sum) / U[i,i]
            except Exception as e:
                # Catch and print any error during the calculation of L[k,i]
                print(f"Error calculating L[{k}][{i}]: {e}")

    # Return the decomposed L and U matrices
    return L, U

def solve_lu(L, U, b):
    n = len(b)
    
    # Forward substitution to solve L*y = b
    y = np.zeros(n)
    try:
        for i in range(n):
            sum = 0
            # Calculate the summation of L[i,j] * y[j]
            for j in range(i):
                sum += L[i,j] * y[j]
            # Calculate the value for y[i]
            y[i] = b[i] - sum
    except Exception as e:
        # Catch and print any error during the forward substitution
        print(f"Error during forward substitution: {e}")
    
    # Back substitution to solve U*x = y
    x = np.zeros(n)
    try:
        for i in range(n-1, -1, -1):
            sum = 0
            # Calculate the summation of U[i,j] * x[j]
            for j in range(i+1, n):
                sum += U[i,j] * x[j]
            # Calculate the value for x[i]
            x[i] = (y[i] - sum) / U[i,i]
    except Exception as e:
        # Catch and print any error during the back substitution
        print(f"Error during back substitution: {e}")
    
    # Return the solution vector x
    return x

def solve_linear_system_lu(A, b):
    try:
        # Perform LU decomposition of matrix A
        L, U = lu_decomposition(A)
        # Solve the linear system using the decomposed L and U matrices
        x = solve_lu(L, U, b)
        # Return the solution vector x, and the L and U matrices
        return x, L, U
    except Exception as e:
        # Catch and print any error during the solution process
        print(f"Error solving the linear system: {e}")
        # Return None for all outputs in case of an error
        return None, None, None

