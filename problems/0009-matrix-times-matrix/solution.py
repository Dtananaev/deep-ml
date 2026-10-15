
import numpy as np
def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    a = np.asarray(a)
    b = np.asarray(b) 
    if a.shape[1] != b.shape[0]:
        return -1
    c = a @ b
    return c