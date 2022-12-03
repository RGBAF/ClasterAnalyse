import numpy as np

matrix = np.matrix([[120, 94, 164],
                    [85, 75.2, 92],
                    [145, 81, 120],
                    [78, 76.8, 86],
                    [70, 75.9, 104]])

avg = lambda matrix_op: sum(matrix_op[0:]) / np.shape(matrix_op)[0]
matrix = np.vstack([matrix, avg(matrix)])
print(matrix)