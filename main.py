#"Функции в Python.Функция с параметром"
def get_matrix( n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([n])
        for j in range(m):
            matrix.append([value])
    print(matrix)


result1 = get_matrix(2, 3, 10)
result2 = get_matrix(3, 4, 25)
result3 = get_matrix(4, 1, 55)
