import numpy as np

def gauss_seidel_method(A, b, x0, tol=1e-10, max_iter=1000):
    # Get the number of rows
    n = len(b)
    
    # Initialize the solution vector with the initial guess
    x = x0.copy()

    # Iterate to solve the system
    try:
        for iteration in range(max_iter):
            x_new = x.copy()  # Create a copy of the current solution

            # Loop over each row
            for i in range(n):
                sum1 = 0
                sum2 = 0
                
                # Calculate sum1 using the updated values in x_new
                for j in range(i):
                    sum1 += A[i,j] * x_new[j]

                # Calculate sum2 using the old values in x
                for j in range(i+1, n):
                    sum2 += A[i,j] * x[j]

                # Update the ith element of the new solution
                x_new[i] = (b[i] - sum1 - sum2) / A[i,i]

            # Calculate the norm (difference between x_new and x) manually
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
