import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
                 
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    if not vectors:
        return True  # Vacuously independent

    v = np.asarray(vectors, dtype=float)
    n_vectors, dim = v.shape

    # More vectors than dimensions in R^m are guaranteed dependent
    if n_vectors > dim:
        return False

    # Full row rank equals number of vectors
    return np.linalg.matrix_rank(v) == n_vectors
