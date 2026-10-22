import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix using Gaussian elimination with partial pivoting.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Create an independent floating-point copy to avoid mutating input
    A = np.array(A, dtype=float, copy=True)
    m, n = A.shape
    
    pivot_row = 0
    
    for col in range(n):
        if pivot_row >= m:
            break
            
        # Find the row with the maximum absolute entry in this column (from pivot_row down)
        rel_idx = np.argmax(np.abs(A[pivot_row:m, col]))
        max_row = pivot_row + int(rel_idx)
        
        # If the largest pivot candidate is below tolerance, the column is linearly dependent
        if np.abs(A[max_row, col]) <= tol:
            continue
            
        # Swap current pivot row with the max row
        if max_row != pivot_row:
            A[[pivot_row, max_row]] = A[[max_row, pivot_row]]
            
        # Eliminate all rows below the pivot row
        pivot_val = A[pivot_row, col]
        for j in range(pivot_row + 1, m):
            factor = A[j, col] / pivot_val
            A[j, col:] -= factor * A[pivot_row, col:]
            
        # Successfully found a linearly independent pivot
        pivot_row += 1

    return pivot_row