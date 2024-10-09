matrixStr = ""
matrixA = []
matrixF = []
K = 0

with open("defaultMatrix.txt") as matrixFile:
	matrixStr = matrixFile.readlines()

def stringToIntMatrixElements(matrix):
	try:
		for i, row in enumerate(matrix):
			for j, col in enumerate(row):
				matrixA[i][j] = int(col)
	except Exception as err:
		print("Error", err)


if matrixStr:
	K = int(matrixStr.pop(0))

	for i, el in enumerate(matrixStr):
		matrixA.append(matrixStr[i].split(" "))

	stringToIntMatrixElements(matrixA)
	matrixF = [row[:] for row in matrixA] 

	# Вычисляем количество нулей в нечетных столбцах области 3
	area_3_odd_cols_zero_count = 0
	for i in range(4, 7):
	    for j in range(1, 7, 2):
	        if matrixF[i][j] == 0:
	            area_3_odd_cols_zero_count += 1

	# Вычисляем сумму чисел в четных строках области 1
	area_1_even_rows_sum = 0
	for i in range(2):
	    for j in range(0, 7, 2):
	        area_1_even_rows_sum += matrixF[i][j]

    # Проверяем условие
	if area_3_odd_cols_zero_count > area_1_even_rows_sum:
	    # Меняем симметрично области 2 и 3 местами
	    for j in range(7):
	        matrixF[2][j], matrixF[4][j] = matrixF[4][j], matrixF[2][j]
	    print("\nОбмен областей 2 и 3 симметрично:")
	    for row in matrixF:
	        print(row)
	else:
	    # Меняем несимметрично области 3 и 4 местами
	    for j in range(7):
	        matrixF[4][j] = matrixF[5][j]
	        matrixF[5][j] = matrixF[4][j]
	    print("\nОбмен областей 3 и 4 несимметрично:")
	    for row in matrixF:
	        print(row)

    # Вычисляем транспонированную матрицу F
	FT = [[matrixF[j][i] for j in range(7)] for i in range(7)]
	print("\nТранспонированная матрица F:")
	for row in FT:
	    print(row)

	# Вычисляем выражение A*F-K*F T
	result = [[0 for _ in range(7)] for _ in range(7)]
	for i in range(7):
	    for j in range(7):
	        for k in range(7):
	            result[i][j] += matrixA[i][k] * matrixF[k][j] - K * FT[k][j]

	print("\nРезультат выражения A*F-K*F T:")
	for row in result:
	    print(row)
else:
	print("The marix is empty")