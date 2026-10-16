import numpy as np

def compute_poly(coeffs: list, x: float)-> float:
    """Compute polynomial."""
    result = 0
    for coeff in coeffs:
        result= result * x + coeff
    return result

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_coeffs = np.asarray(g_coeffs)
    h_coeffs = np.asarray(h_coeffs)
    g_idx =np.arange(len(g_coeffs))[::-1]
    h_idx = np.arange(len(h_coeffs))[::-1]

    # We drop last term as derivative is zero
    dg_coeffs = (g_idx * g_coeffs)[:-1]
    dh_coeffs = (h_idx * h_coeffs)[:-1]

    # Get polynomial values
    g_x = compute_poly(coeffs=g_coeffs, x=x)
    h_x = compute_poly(coeffs=h_coeffs, x=x)
    # Get derivative values
    dg_x = compute_poly(coeffs=dg_coeffs, x=x)
    dh_x = compute_poly(coeffs=dh_coeffs, x=x)

    f_x = (dg_x*h_x - g_x * dh_x) / h_x ** 2 
    return f_x
  