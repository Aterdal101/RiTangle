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

def multiply_rows(matrix1):
    result = []
    for row in matrix1:
        product = 1
        for num in row:
            product *= num
        result.append(product)
    return result

row_products1 = multiply_rows(matrix1)
row_products2 = multiply_rows(matrix2)

def calculate_probability(row_products1, row_products2):
    total_elements = len(row_products1)
    count = sum(1 for value1, value2 in zip(row_products1, row_products2) if value1 < value2)
    probability = count / total_elements
    return probability

print(calculate_probability(row_products1, row_products2))