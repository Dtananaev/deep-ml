import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	result = {}
	gradient = np.asarray(gradient, dtype=np.float32)
	result["magnitude"] = np.linalg.norm(gradient)
	result["direction"] = gradient
	result["descent_direction"] = -gradient
	if result["magnitude"] != 0:
		result["direction"] /= result["magnitude"]
		result["descent_direction"] /= result["magnitude"]
	return result