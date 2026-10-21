def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b = matrix[0][0], matrix[0][1]
    c, d =matrix[1][0], matrix[1][1]

    determinant = a * d - c * b
    if determinant == 0:
        return None
    s = float( 1. / determinant)
    return [[s * d, -s * b], [-s * c, s * a]]

