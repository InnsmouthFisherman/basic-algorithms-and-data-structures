# умножение матриц
# число столбцов матрицы а должно быть равно числу строк матрицы б
# цмножая матрицу следует умножить все числа каждой строки матрицы а на все числа каждого столбца матрицы б, а произведения сложить

mat1 = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
mat2 = [[5,8,1],
        [6,7,3],
        [4,5,9]]

def matrix_multiply(a,b):	
	if len(a) == len(b[0]) or len(b) == len(a[0]):
		if len(a) < len(b) and len(a[0]) > len(b[0]):
			res = [[0 for x in range(len(a[0]))] for y in range(len(a))]
		else:
			res = [[0 for x in range(len(b[0]))] for y in range(len(b))]
		
		for i in range(len(a)):
			for j in range(len(b[0])):
				for k in range(len(b)):
					res[i][j] += a[i][k] * b[k][j]
		return res
		
print(matrix_multiply(mat1,mat2))
