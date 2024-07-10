import numpy as np

def gaussian_elimination(A, b):
    try:
        n = len(b)  # Get the number of elements in vector b, which is the size of the system
        A = A.astype(float)  # Convert matrix A to float type to handle division properly
        b = b.astype(float)  # Convert vector b to float type for consistency

        # Forward elimination process to transform A to an upper triangular matrix
        for j in range(n):
            if A[j, j] == 0:  # Check if the pivot element is zero
                raise ValueError("Matrix is singular or nearly singular")
            for i in range(j + 1, n):  # Loop over rows below the pivot row
                if A[i, j] != 0:  # If the element below the pivot is non-zero
                    factor = A[i, j] / A[j, j]  # Calculate the factor to zero out the element
                    A[i, j:] -= factor * A[j, j:]  # Subtract the factor times the pivot row from the current row
                    b[i] -= factor * b[j]  # Adjust the corresponding element in vector b

        # Back substitution process to find the solution vector x
        x = np.zeros_like(b)  # Initialize the solution vector with zeros
        for i in range(n - 1, -1, -1):  # Loop backward from the last row to the first row
            if A[i, i] == 0:  # Check if the diagonal element is zero
                raise ValueError("Matrix is singular or nearly singular")
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]  # Calculate the value of x[i]

        return x  # Return the solution vector
    
    except ValueError as e:  # Catch any ValueError raised
        print("Error:", e)  # Print the error message
        return None  # Return None to indicate that no solution was found