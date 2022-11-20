#  Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random

matrixSize = random.randint(5, 10)
print(f'размер матрицы = {matrixSize}')

matrixList = [None]*matrixSize

for i in range(matrixSize):
    matrixList[i] = list(random.randint(2, 15) for _ in range(matrixSize))

print("Квадратная матрица:")
for row in matrixList:
    print(row)

diagonalList = []
for i in range(len(matrixList)):
    diagonalList.append(matrixList[i][i])
print(f'Элементы главной диагонали: \n {diagonalList}')
diagonalSum = sum(diagonalList)
print(f'Сумма элементов главной диагонали: {diagonalSum}')

compareList = []
for row in matrixList:
    if sum(row) > diagonalSum:
        compareList.append(row)

if len(compareList) == 0:
    print("нет таких элементов")
else:
    print("строки, сумма элементов которых превосходит сумму главной диагонали матрицы:")
    for row in compareList:
        print(f'{row} сумма = {sum(row)}')
