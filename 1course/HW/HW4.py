from random import randint


def mat_print(mat):
    for line in mat:
        print(*line)
    print("\n")


def generate(n, m, random=True):
    if random:
        return [[randint(0, 9) for i in range(m)] for j in range(n)]
    else:
        return [[0 for i in range(m)] for j in range(m)]


def simple(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = 2
            elif i > j:
                matrix[i][j] = 0
    return matrix


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]


def rotate90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def maximal(matrix, row=False, col=False):
    if row and not col:
        return sorted(matrix, key=sum)[-1]

    if not row and col:
        matrix_rotated = rotate90(matrix)
        return sorted(matrix_rotated, key=sum)[-1]

    if not row and not col:
        return max(sum(matrix, []))

    if row and col:
        matrix_rotated = rotate90(matrix)
        max_row_index = matrix.index(sorted(matrix, key=sum)[-1])
        max_col_index = matrix_rotated.index(sorted(matrix_rotated, key=sum)[-1])
        return [matrix[max_row_index][max_col_index], max_row_index, max_col_index]


def sub(matrix, r1, r2, c1, c2):
    return [[matrix[i][j] for j in range(c1, c2 + 1)] for i in range(r1, r2 + 1)]


def rotate(matrix, r1, r2, c1, c2):
    if r2 - r1 == c2 - c1:
        transposed_sub_mat = transpose(sub(matrix, r1, r2, c1, c2))
        return matrix[:r1] + [matrix[i][:c1] + transposed_sub_mat[i - r1] + matrix[i][c2 + 1:] for i in
                              range(r1, r2 + 1)] + matrix[r2 + 1:]


sample_matrix = [[3, 4, 1, 2, 5],
                 [4, 5, 2, 8, 9],
                 [9, 1, 3, 7, 1],
                 [4, 5, 2, 8, 9]]

sample_matrix1 = [[3, 4, 1, 2, 5],
                  [4, 5, 2, 8, 9],
                  [9, 1, 3, 7, 1],
                  [4, 5, 2, 8, 9]]

simp_sample_matrix = [[10, 2, 3],
                      [1, 11, 6]]

rotate_samp = [[10, 2, 3],
               [1, 11, 6],
               [5, 4, 9]]

sub_sample_matrix = [[12, 3, 5, -7, 8],
                     [1, 3, 4, 0, 9],
                     [11, 15, -3, 1, 9],
                     [7, 3, 4, 1, 2],
                     [18, 9, -3, -2, -1]]

mat_print(generate(4, 5, True))
mat_print(simple(sample_matrix))
print(maximal(sample_matrix1, row=True, col=True))
mat_print(sub(sub_sample_matrix, 1, 4, 1, 3))
mat_print(rotate(rotate_samp, 0, 1, 0, 1))
