import itertools 
from itertools import permutations
import numpy as np
fmn = [1, 2, 3, 4, 5, 6, 7, 8]
FM = itertools.permutations(fmn,5)
permutation1 = list(FM)
matrix1 = np.array(permutation1).reshape(len(permutation1), -1)

SM = itertools.permutations(fmn,3)
permutation2 = list(SM)
matrix2 = np.array(permutation2).reshape(len(permutation2), -1)
def calculate_probability(matrix1, matrix2):
    total_elements = 0
    count = 0

    for row1, row2 in zip(matrix1, matrix2):
        for value1, value2 in zip(row1, row2):
            total_elements += 1
            if value1 < value2:
                count += 1
    probability = count / total_elements
    return probability
print(calculate_probability(matrix1, matrix2))


