import numpy as np  # Import the NumPy library for numerical operations
from gaussian_elimination import gaussian_elimination  # Import the gaussian_elimination function from the defined module
from LU import solve_linear_system_lu
from jacobi import jacobi_method

def input_augMatrix():
    # Prompt the user to input the size of the square matrix A
    n = int(input("Enter the size of square matrix A: "))
    
    matrix = []  # Initialize an empty list to store the rows of the matrix A
    col_vector = []  # Initialize an empty list to store the entries of vector b
    
    # Loop to input the entries of the matrix A
    for i in range(n):
        rows = []  # Initialize an empty list to store the current row entries
        for j in range(n):
            row_entry = float(input(f"Enter A[{i},{j}]: "))  # Prompt the user to input each element of the matrix A
            rows.append(row_entry)  # Append the element to the current row
        matrix.append(rows)  # Append the current row to the matrix

    # Loop to input the entries of the vector b
    for k in range(n):
        colvec_entry = float(input(f"Enter b[{k}]: "))  # Prompt the user to input each element of the vector b
        col_vector.append(colvec_entry)  # Append the element to the vector
    
    # Convert the lists to NumPy arrays and return them
    return np.array(matrix), np.array(col_vector)

# Call the function to input the augmented matrix and vector
C, d = input_augMatrix()


# Gaussian Elimination (Uncomment the code below to implement Gaussian Elimination Method)


# Call the Gaussian elimination function to solve the system
#solution = gaussian_elimination(C, d)

#if solution is not None:  # Check if a solution was found
#   print("Solution x:", solution)  # Print the solution
#else:
#    print("No solution found or matrix is singular.")  # Print a message indicating no solution was found



# LU Decomposition (Uncomment the code below to implement LU Decomposition Method)

# Call the LU Decomposition function to solve the system
#solution = solve_linear_system_lu(C, d)

#if solution is not None:  # Check if a solution was found
#    print("x, L, U (respectively):", solution)  # Print the solution
#else:
#    print("No solution found or matrix is singular.")  # Print a message indicating no solution was found



# Jacobi Method (Uncomment the code below to implement Jacobi Method)

x0 = np.zeros_like(d)
try:
    x = jacobi_method(C, d, x0)
    print("Solution x:", x)
except Exception as e:
    print(f"Error solving the linear system with Jacobi method: {e}")
