def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	row_size = len(matrix)
	cols_size = len(matrix[0])
	if mode == "row":
		means = [sum(row) /  cols_size for row in matrix]
	elif mode == "column":
		means = [0] * cols_size
		for row in matrix:
			means = [v + m for v, m in zip(row, means)]
		means = [val / row_size for val in means]
	return means