# A coding assessment for a company interview
"""
inputMat, represents the matrix of N*M, where N is inputMat_row and M is inputMat_col.
"""
def funcRotate(inputMat):
	# Write your code here

	N, M = len(inputMat), len(inputMat[0])

	# Initialize the resulting matrix of size M*N
	out_mat = [[False for i in range(N)] for j in range(M)]

	for i, line in enumerate(inputMat):
		for j, num in enumerate(line):
			out_mat[j][N-i-1] = num
	return out_mat

def main():
	#input for inputMat
	inputMat = []
	inputMat_rows,inputMat_cols  = map(int, input("Input: ").split())
	for idx in range(inputMat_rows):
		inputMat.append(list(map(int, input().split())))
	
	
	result = funcRotate(inputMat)
	for row in result:
		for num in row:
			print(num, end=' ')
		print()
	# print(result)	

if __name__ == "__main__":
	# Initialize a matrix of size 3*3, with the first two items 
    # in the matrix as the number of rows and columns respectively.
    # The rest of the items are the actual matrix values.
    # inputMat = 
	# print(funcRotate([3, 3, 
	# 	[1, 2, 3],
	# 	[4, 5, 6],
	# 	[7, 8, 9]
	# ]))
    main()