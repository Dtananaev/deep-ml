import numpy as np
def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	p = 1.0 / n
	values = np.arange(n)+1
	sq_values = values ** 2
	expected_value = p * np.sum(values)
	sq_expected_value = p *  np.sum(sq_values)
	variance = sq_expected_value - expected_value**2
	return expected_value, variance
