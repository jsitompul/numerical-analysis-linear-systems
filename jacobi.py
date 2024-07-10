import numpy as np

def jacobi_method(A, b, x0, tol=1e-10, max_iter=1000):
    # Get the number of rows
    n = len(b)
    
    # Initialize the solution vector with the initial guess
    x = x0.copy()

    # Initialize the diagonal and remainder matrices
    D = np.zeros(n)
    R = np.zeros((n, n))

    # Extract the diagonal elements of A into D
    try:
        for i in range(n):
            D[i] = A[i,i]
    except Exception as e:
        print(f"Error extracting diagonal elements: {e}")

    # Compute the remainder matrix R
    try:
        for i in range(n):
            for j in range(n):
                if i != j:
                    R[i,j] = A[i,j]
                else:
                    R[i,j] = 0
    except Exception as e:
        print(f"Error computing remainder matrix R: {e}")

    # Iterate to solve the system
    try:
        for iteration in range(max_iter):
            x_new = np.zeros(n)

            # Compute the new x values
            for i in range(n):
                sum = 0
                for j in range(n):
                    if i != j:
                        sum += R[i,j] * x[j]
                x_new[i] = (b[i] - sum) / D[i]

            # Calculate the norm (difference between x_new and x)
            norm = 0
            for i in range(n):
                norm += (x_new[i] - x[i]) ** 2
            norm = norm ** 0.5

            # Check for convergence
            if norm < tol:
                return x_new

            # Update x for the next iteration
            x = x_new

    except Exception as e:
        print(f"Error during iteration: {e}")

    # Return the last computed x if max iterations reached without convergence
    return x
