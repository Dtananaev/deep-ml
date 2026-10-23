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
    # Your code here
    vectors = np.asarray(vectors)
    normalized_v = vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)
    # [N, m] @ [m, N] = NxN
    dot_product = normalized_v @ normalized_v.T
    res = np.sum(dot_product - np.eye(vectors.shape[0]))

    return res == 0.0
