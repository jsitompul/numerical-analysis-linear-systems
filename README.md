# Numerical Analysis Linear Systems

This project demonstrates the implementation of four numerical methods to solve linear systems:` Gaussian Elimination`, `LU Decomposition`, `Jacobi Method`, and `Gauss-Seidel` Method. The code is structured with separate modules for each method, and a main script (`main.py`) to call and test these methods.


## Author

Jimmy Sitompul

## Project Structure

- `main.py`: The main script that interacts with the user, takes input for the linear equations system (square matrix 𝐴 and vector 𝑏), and calls the respective methods.
- `gaussian_elimination.py`: Contains the implementation of the Gaussian Elimination method.
- `LU.py`: Contains the implementation of the LU Decomposition method.
- `jacobi.py`: Contains the implementation of the Jacobi Method.
- `gauss_seidel.py`: Contains the implementation of the Gauss-Seidel Method.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/numerical-analysis-linear-systems.git
   cd numerical-analysis-linear-systems
   ```
   
2. Ensure you have NumPy installed:

  ```bash
  pip install numpy
  ```

3. Run the main script:

  ```bash
  python main.py
  ```

4. Follow the prompts to enter the size of the square matrix 𝐴 and the entries of the matrix 𝐴 and vector 𝑏.

5. Uncomment the desired method in main.py to solve the linear system using that method.

## Code Explanation (main.py)

The following is the function to input the system of linear equations (a square matrix and a vector)

  ```bash
  def input_linearEquations():
    # Prompt the user to input the size of the system of linear equations
    n = int(input("Enter the size of the linear equations system: "))
  ```

The following loops to input the entries of the square matrix 

  ```bash
  square_matrix = []  # Initialize an empty list to store the rows of the matrix

  for i in range(n):
    rows = []  # Initialize an empty list to store the current row entries
    for j in range(n):
      row_entry = float(input(f"Enter A[{i},{j}]: "))  # Prompt the user to input each element of the matrix A
      rows.append(row_entry)  # Append the element to the current row
    square_matrix.append(rows)  # Append the current row to the matrix
  ```

The following loops to input the entries of the vector

  ```bash
  col_vector = []  # Initialize an empty list to store the entries of the vector

  for k in range(n):
    colvec_entry = float(input(f"Enter b[{k}]: "))  # Prompt the user to input each element of the vector b
    col_vector.append(colvec_entry)  # Append the element to the vector
  ```

The following converts the lists to NumPy arrays and returns them
    ```bash
    return np.array(square_matrix), np.array(col_vector)
    ```

## Methods

### Gaussian Elimination

This method is implemented in gaussian_elimination.py. It performs forward elimination to transform the matrix into an upper triangular form and then applies back substitution to find the solution.

### LU Decomposition

This method is implemented in LU.py. It decomposes the matrix 𝐴 into a lower triangular matrix 𝐿 and an upper triangular matrix 𝑈, then solves the system using forward and back substitution.

### Jacobi Method

This iterative method is implemented in jacobi.py. It updates the solution vector based on the previous iteration until convergence is achieved within a specified tolerance.

### Gauss-Seidel Method

This iterative method is implemented in gauss_seidel.py. It updates the solution vector using the most recent values, which often converges faster than the Jacobi method.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by "Numerical Analysis: Mathematics of Scientific Computing (Third Edition)" by `David Kincaid` and `Ward Cheney`.
- `numpy` library for providing efficient numerical operations.


