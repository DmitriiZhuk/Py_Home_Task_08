# В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
#  Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random
groups = random.randint(5, 10)

groupsList = [None]*groups
for i in range(len(groupsList)):
    groupsList[i] = list(random.randint(2, 5) for _ in range(random.randint(20, 30)))

print(f'оценки всех групп:')
for row in groupsList:
    print(row)

averageMarkList = []
for row in groupsList:
    averageMarkList.append(sum(row) / len(row))
print(f'средние оценки всех групп: \n {averageMarkList}')

print(f'наилучший средний балл: {max(averageMarkList)}')
print(f'группа с наилучшим средним баллом: {averageMarkList.index(max(averageMarkList)) + 1 }')
