def rotatedImage(matrix):
	# Write your code here
	new_matrix = []
	reverse_matrix = matrix.reverse()
	for i in range(len(matrix)):
		for ii in range(len(matrix[i])):
			new_matrix.append(reverse_matrix[ii][i])
	print(new_matrix)
	return new_matrix

def main():
	#input for matrix
	matrix = [[2, 1], [3, 4]]
	matrix_rows,matrix_cols  = map(int, input().split())
	for idx in range(matrix_rows):
		matrix.append(list(map(int, input().split())))
	
	
	result = rotatedImage(matrix)
	for idx in range(len(result)):
		temp_res = result[idx]
		print(" ".join([str(res) for res in temp_res]))	

if __name__ == "__main__":
	main()