import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    result = x
    derivative = 1
    for func in np.asarray(functions)[::-1]:
        if func == 'square':
            derivative *= 2 * result
            result = result **2

        if func == 'sin':
            derivative *= np.cos(result) 
            result = np.sin(result)
        if func == 'exp':
            derivative *= np.exp(result)
            result = np.exp(result)
        if func == 'log':
            derivative *= 1.0 / result
            result = np.log(result)


    return derivative
