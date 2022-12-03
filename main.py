import numpy as np

# matrix = np.matrix([[120, 94, 164],
#                     [85, 75.2, 92],
#                     [145, 81, 120],
#                     [78, 76.8, 86],
#                     [70, 75.9, 104]])
matrix = np.matrix([[120, 108, 104],
                    [60, 58, 58],
                    [145, 145, 131],
                    [30, 29, 24],
                    [29, 31, 17]])

avg = lambda matrix_op: sum(matrix_op[0:]) / np.shape(matrix_op)[0]
err_avg = lambda matrix_op: np.power((sum(np.power((matrix_op[0:] - avg(matrix_op)), 2)) / np.shape(matrix_op)[0]), 0.5)
matZ = lambda matrix_op: (matrix_op - avg(matrix_op)) / err_avg(matrix_op)

matrix_f = np.vstack([matrix, avg(matrix), err_avg(matrix)])
print(matrix_f)
print(matZ(matrix))
