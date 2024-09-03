# Compute Log Canonical Threshold and Multiplicity

This repository contains a Python function `compute_lct` that computes the log canonical threshold (LCT) and its multiplicity for a function that is a product of linear forms. If the coefficients of the linear forms are real numbers then the result equals also the real log canonical threshold and its multiplicity from Singular Learning Theory. The function uses linear algebra and combinatorial methods to analyze intersections of hyperplanes defined by the linear forms.

## Function Overview

### `compute_lct(A, s)`

#### Parameters:
- `A` (matrix): A matrix representing the coefficients of the linear forms that define the hyperplanes. Each row of `A` corresponds to the normal vector of a hyperplane in the ambient space.
- `s` (vector): A vector of positive integers representing the exponents associated with each linear form.

#### Returns:
- `lambda_min` (float): The minimum value of the ratio of the codimension of an intersection `W` to the sum of the exponents `s_j` corresponding to the hyperplanes that contain `W`.
- `m` (int): The multiplicity of the LCT, defined as the maximum length of a chain of intersections where `lambda_min` is achieved.

### How It Works:
1. **Validation**: The function checks if the length of vector `s` matches the number of rows in matrix `A`. If not, it raises a `ValueError`.
2. **Codimension Calculation**: A helper function `codim(W)` calculates the codimension of an intersection `W`.
3. **Sum of Exponents Calculation**: The function `s_function(W)` computes the sum of the exponents `s_j` for all hyperplanes that contain the intersection `W`.
4. **Intersections Calculation**: The function computes all possible intersections of the hyperplanes by considering all combinations of the rows of `A`.
5. **Remove Duplicate Intersections**: Duplicate intersections are removed to ensure unique analysis.
6. **Compute `lambda_min`**: The function calculates `lambda_min` as the minimum of `codim(W) / s_function(W)` across all intersections.
7. **Filter Intersections**: It then filters the intersections where this minimum is achieved.
8. **Chain Length Calculation**: The function calculates the maximum length of a chain of these filtered intersections to determine the multiplicity `m`.
9. **Return Values**: Finally, it returns `lambda_min` and `m`.

## Example Usage

```python
# Import the required libraries
from sage.all import Matrix, vector

# Define the matrix of coefficients for the hyperplanes
A = Matrix([[1, 0], [0, 1], [1, 1], [1, -1]])

# Define the vector of exponents
s = vector([1, 1, 1, 1])

# Compute the LCT and multiplicity
lambda_min, m = compute_lct(A, s)

print(f"Log Canonical Threshold (lambda_min): {lambda_min}")
print(f"Multiplicity (m): {m}")
