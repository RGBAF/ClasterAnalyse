import numpy as np

matrix = np.matrix([[120, 108, 104],
                    [60, 58, 58],
                    [145, 145, 131],
                    [30, 29, 24],
                    [29, 31, 17]])

avg = lambda matrix_op: sum(matrix_op[0:]) / np.shape(matrix_op)[0]
err_avg = lambda matrix_op: np.power((sum(np.power((matrix_op[0:] - avg(matrix_op)), 2)) / np.shape(matrix_op)[0]), 0.5)
matz = lambda matrix_op: (matrix_op - avg(matrix_op)) / err_avg(matrix_op)
d = lambda z, i, j: np.sum(np.power((z[i] - z[j]), 2))
matrix_f = np.vstack([matrix, avg(matrix), err_avg(matrix)])
print(matrix_f, '\n')
matrix_z = matz(matrix)
print(f'Матрица Z:\n{matrix_z}\n')
group_list = [str(i) for i in range(1, matrix.shape[0] + 1)]
D = np.ones((matrix.shape[0], matrix.shape[0]))
for i in range(D.shape[0]):
    D[i:, i] = np.nan
    # D[i, i] = 0
    for j in range(i+1, D.shape[0]):
        D[i, j] = d(matrix_z, i, j)
while len(group_list) > 1:
    print(group_list, '\n', D, '\n')
    x = np.nanargmin(D) // D.shape[0]
    y = np.nanargmin(D) % D.shape[0]
    group_list[x] = f'{group_list[x]} + {group_list[y]}'
    group_list.pop(y)
    for i in range(D.shape[0]):
        D[i][x] = max(D[i][x], D[i][y])
    D = np.delete(D, y, axis=0)
    D = np.delete(D, y, axis=1)
