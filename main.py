"""
	С клавиатуры вводится два числа K и N. 
	Квадратная матрица А(N,N) заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное, введенное из файла. 
	Условно матрица имеет вид:

    20.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если количество нулей в нечетных столбцах в области 3 больше, чем сумма чисел в четных строках в области 1, то поменять симметрично 
    области 2 и 3 местами, иначе 3 и 4 поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: A*F-K*F T . 
    Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import math

def readFile(file_name):
    with open(file_name) as matrixFile:
        matrixStr = matrixFile.readlines()
        return matrixStr

def strip_matrix(matrix):
    striped_matrix = list(matrix)

    for ind, val in enumerate(matrix):
        striped_matrix[ind] = val.strip()

    return striped_matrix

def prompt_number(console_text = "Введите число"):
    str = input(console_text)
    is_number = str.isdigit()

    if not is_number:
        return prompt_number(console_text)

    return int(str)

def parse_matrix_to_number(matrix):
    splited_mat = list(matrix)
    parsed_matrix = list()

    for i, val in enumerate(splited_mat):
        splitted_row = val.split()
        new_matrix = list()

        for j, item in enumerate(splitted_row):
            is_digit = item.lstrip("-+").isdigit()

            if not is_digit:
                print(f"Это не число - {item}")
                quit()

            parsedValue = int(item)

            if(parsedValue < -10  or parsedValue > 10):
                print(f"Значение выходит за лимиты [-10;10] {item}")
                quit()

            new_matrix.append(parsedValue)

        parsed_matrix.append(new_matrix)

    return parsed_matrix

def get_matrix_area(matrix, end_row, end_col, start_row = 0, start_col = 0):
    matrix_area = list()

    for i in range(start_row, end_row):
        row = list()
        for j in range(start_col, end_col):
            row.append(matrix[i][j])
        matrix_area.append(row)

    return matrix_area

def divide_matrix_into_areas(matrix):
    max_cols = math.ceil( len(matrix[0]) / 2 )
    max_rows = math.ceil( len(matrix) / 2 )
    count_rows = len(matrix)
    count_cols = len(matrix[0])

    matrix_area_1 = get_matrix_area(matrix, end_row=max_rows, end_col=max_cols)
    matrix_area_2 = get_matrix_area(matrix, end_row=max_rows, end_col=count_cols, start_col=max_cols)
    matrix_area_3 = get_matrix_area(matrix, start_row=max_rows, end_row=count_rows, end_col=max_cols)
    matrix_area_4 = get_matrix_area(matrix, start_row=max_rows, start_col=max_cols, end_row=count_rows, end_col=count_cols)

    return matrix_area_1, matrix_area_2, matrix_area_3, matrix_area_4
    
def get_count_zero_in_matrix_area(matrix):
    count_zero = 0

    for row in matrix:
        for col in range(0, len(row), 2):
            if row[col] == 0:
                count_zero += 1

    return count_zero

def get_sum_number_matrix_area(matrix):
    count_sum = 0

    for row in range(1, len(matrix), 2):
        for col in matrix[row]:
            count_sum += col

    return count_sum

def concat_areas(area_1, area_2):
    concated_areas = list()

    len_area_1 = len(area_1)
    len_area_2 = len(area_2)
    max_len_areas = max(len_area_1, len_area_2)

    for i in range(max_len_areas):
        row = []
        if i < len_area_1:
            row.extend(area_1[i])
        if i < len_area_2:
            row.extend(area_2[i])

        concated_areas.append(row)

    return concated_areas

def repleacing_areas(areas, count_zero, sum_number):
    swaped_matrix = []

    if count_zero > sum_number:
        concated_areas_1_with_3 = concat_areas(areas[0], areas[2])
        concated_areas_2_with_4 = concat_areas(areas[1], areas[3])
        swaped_matrix = concated_areas_1_with_3 + concated_areas_2_with_4
        print("Замена областе 2 и 3 местами")
    else:
        concated_areas_1_with_2 = concat_areas(areas[0], areas[1])
        concated_areas_4_with_3 = concat_areas(areas[3], areas[2])
        swaped_matrix = concated_areas_1_with_2 + concated_areas_4_with_3
        print("Замена областе 3 и 4 местами")

    return swaped_matrix

def matrix_multiply(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    if cols_a != rows_b:
        print("Ошибка: Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")
        quit()

    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result_matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def matrix_subtract(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0
    
    if rows_a != rows_b or cols_a != cols_b:
        print("Ошибка: Матрицы должны иметь одинаковые размеры для вычитания.")
        quit()

    result_matrix = [[0 for _ in range(cols_a)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_a):
            result_matrix[i][j] = matrix_a[i][j] - matrix_b[i][j]
    
    return result_matrix

def scalar_multiply(matrix, scalar):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0 

    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] * scalar

    return result_matrix

def show_matrix(matrix):
    for row in matrix:
        print(row)            

def main():
    # НАИМЕНОВАНИЕ ФАЙЛА, СОДЕРЖАЩЕГО МАТРИЦУ
    file_name = "defaultMatrix.txt"

    default_matrix = readFile(file_name)
    striped_matrix = strip_matrix(default_matrix)

    K = prompt_number("Введите число K")
    N = prompt_number("Введите число N")

    parsed_matrix = parse_matrix_to_number(striped_matrix)
    mat_A = parsed_matrix
    print(f"Матрица из файла {file_name}")
    show_matrix(striped_matrix)
    print('\n')

    mat_F = mat_A[:]
    print("Матрица F на основе матрицы A")
    show_matrix(mat_F)
    print('\n')

    m_area_1, m_area_2, m_area_3, m_area_4 = divide_matrix_into_areas(mat_A)
    print("Разделение на области матрицы F")
    print("Область 1")
    show_matrix(m_area_1)
    print('\n')
    print("Область 2")
    show_matrix(m_area_2)
    print('\n')
    print("Область 3")
    show_matrix(m_area_3)
    print('\n')
    print("Область 4")
    show_matrix(m_area_4)
    print('\n')

    count_zero_odd_cols_area_3 = get_count_zero_in_matrix_area(m_area_3)
    print(f"Количество нулей в нечетных столбцах в области 3: {count_zero_odd_cols_area_3}")
    print("\n")
    sum_number_even_rows_area_1 = get_sum_number_matrix_area(m_area_1)
    print(f"Сумма чисел в четных строках в области 1: {sum_number_even_rows_area_1}")
    print("\n")

    mat_F = repleacing_areas([m_area_1, m_area_2, m_area_3, m_area_4], 
                                     count_zero_odd_cols_area_3, 
                                     sum_number_even_rows_area_1)
    show_matrix(mat_F)
    print("\n")

    multiply_matrix_A_with_B = matrix_multiply(mat_A, mat_F)
    print("Вычисление A*B")
    show_matrix(multiply_matrix_A_with_B)
    print("\n")

    transposed_matrix_F = transpose_matrix(mat_F)
    print("Транспонированная матрица F")
    show_matrix(transposed_matrix_F)
    print("\n")

    matrix_K_with_F = scalar_multiply(transposed_matrix_F, K)
    print("Умножение K на транспоринованную матрицу F")
    show_matrix(matrix_K_with_F)
    print("\n")

    subtracted_matrix = matrix_subtract(multiply_matrix_A_with_B, matrix_K_with_F)
    print("Вычитание A*F-K*F^T")
    show_matrix(subtracted_matrix)
    print("\n")

    print("Результат:")
    show_matrix(subtracted_matrix)
    
if __name__ == "__main__":
    main()