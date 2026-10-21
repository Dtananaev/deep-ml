import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as a list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    n = len(matrix)
    if n == 0:
        return 0.0, 0.0
        
    # Trace is simply the sum of diagonal entries
    trace = float(sum(matrix[i][i] for i in range(n)))
    
    if n == 1:
        return float(matrix[0][0]), trace
    
    if n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return float(det), trace

    # LU Decomposition with Partial Pivoting (PLU)
    U = np.array(matrix, dtype=float)
    sign = 1.0  # Track sign changes caused by row swaps

    for i in range(n):
        # Pivot selection: find largest absolute value in column i
        pivot_row = i + int(np.argmax(np.abs(U[i:, i])))
        
        if np.isclose(U[pivot_row, i], 0.0):
            return 0.0, trace  # Singular matrix has determinant 0
            
        if pivot_row != i:
            # Swap rows in U and flip determinant sign
            U[[i, pivot_row]] = U[[pivot_row, i]]
            sign = -sign

        # Elimination
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            U[j, i:] -= factor * U[i, i:]

    # Determinant is sign * product of diagonal entries
    determinant = float(sign * np.prod(np.diag(U)))

    return determinant, trace