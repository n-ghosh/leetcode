# A coding assessment for a company interview

def matrix_minmax(inputMat):
    '''Finds a value in the matrix inputMat that is both 
    the maximum of its column and the minimum of its row.
    Returns that value, or -1 if not found. '''
    '''inputMat
    0 1 2 3
    4 5 6 7 
    8 9 0 1 '''

    # option 1: store the maxes/mins of each in a dictionary then compare O(M*N + M+N)
    # option 2: make a transpose so I can call max(row) for each row of the transpose / each col of the original
    # option 3: loop through each row: find its min, then check if it's the max in that column. O(M*N)
    for i, row in enumerate(inputMat):
        # find the min value & index of each row
        min_value = inputMat[i][0]
        min_index = 0
        for j, num in enumerate(row):
            if num < min_value:
                min_value = num
                min_index = j
        # loop through this column to find if it's the max
        for i2 in range(len(inputMat)):
            # if there is a greater, break the inner loop
            if inputMat[i2][min_index] > min_value:
                min_value = False
                break
            # otherwise we have a winner
            if i2 == len(inputMat) - 1:
                return min_value
    return -1

# no minmax
mat1 = [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 0, 1]]
assert(matrix_minmax(mat1) == -1)

# 6 is the min of its row & max of its col
mat2 = [[9, 8, 7, 6],
        [6, 7, 8, 4],
        [4, 3, 2, 1]]
assert(matrix_minmax(mat2) == 6)


# Test random
import random
num_rows = 13
num_cols = 11
for n in range(num_rows):
    for m in range(num_cols):
        mat = [[random.randint(0,100) for i in range(num_cols)] for j in range(num_rows)]
        
        sol = random.randint(10, 90)
        mat[n][m] = sol
        
        for i in range(num_rows):
            if i != n:
                mat[i][m] = random.randint(0, sol-1)
        
        for j in range(num_cols):
            if j != m:
                mat[n][j] = random.randint(sol+1, 100)

        try:
            ans = matrix_minmax(mat)
            assert(ans == sol)
        except AssertionError:
            print(f"Failed test: expected {sol}, received {ans}, for: ")
            for line in mat:
                print(line)
        except Exception as e:
            print(f"Failed test: expected {sol}, error {e}, for {num_rows}x{num_cols}")
            raise e
        