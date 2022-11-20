# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

import random

qtyDaysList = [31, 30, 31, 31, 30]
nameDaysList = ["Май", "Июнь", "Июль", "Август", "Сентябрь"]


tempsList = [None]*(len(qtyDaysList))
for i in range(len(tempsList)):
    # расчет средней дневной температуры в интервале от 15 до 30 градусов, с округлением до 2х знаков
    # dayTemp = round(random.uniform(15.00, 30.00), 2)
    tempsList[i] = list(round(random.uniform(15.00, 30.00), 2)
                        for _ in range(qtyDaysList[i]))

print("Средние дневные температуры:")
for row in tempsList:
    print(f'{nameDaysList[tempsList.index(row)]} : {row} \n')

flatTempsList = sum(tempsList, [])
print(
    f' Одномерный массив температур с {nameDaysList[0]} по {nameDaysList[-1]} : {flatTempsList}')

daysStep = 7
sevenDaysTempList = []
for i in range(len(flatTempsList) - daysStep):
    weekTemp = 0
    for j in range(daysStep):
        daysNum = i+j
        weekTemp = weekTemp + flatTempsList[daysNum]
    sevenDaysTempList.append(weekTemp)
print(f"\n Семидневные промежутки температуры:")
print(sevenDaysTempList)

maxSevenDays, minSevenDays = max(sevenDaysTempList), min(sevenDaysTempList)
print(
    f'\n Максимальный промежуток 7дневной температуры: {maxSevenDays}, минимальный промежуток 7дневной температуры {minSevenDays}')

maxIndex, minIndex = sevenDaysTempList.index(
    maxSevenDays), sevenDaysTempList.index(minSevenDays)
print(
    f'\n Индекс максимального промежутка 7дневной температуры: {maxIndex} (день), Индекс минимального промежутка 7дневной температуры {minIndex} (день)')


def printIntervals(index, type):
    qtySumDaysList = []
    daysSum = 0
    for i in range(len(qtyDaysList)):
        daysSum = daysSum + qtyDaysList[i]
        qtySumDaysList.append(daysSum)

    print()
    print(qtySumDaysList)

    monthIn = 0
    for row in qtySumDaysList:
        if (index <= row):
            monthIn = qtySumDaysList.index(row)
            break

    print(f'({monthIn+1}) - месяц входа {type} индекса')

    # случай 1 = все в мае
    if index < qtySumDaysList[0] and ((index + daysStep) <= qtySumDaysList[0]):
        print("случай 1 = все в мае")
        print(
            f'Промежуток {type} темп = с {index} {nameDaysList[0]} по {index + daysStep} {nameDaysList[0]}')

    # случай 1.1 = конец мая переход в июнь
    elif index <= qtySumDaysList[0] and ((index + daysStep) >= qtySumDaysList[0]):
        print("случай 1.1 = конец мая переход в июнь")
        print(
            f'Промежуток {type} темп = с {index} {nameDaysList[0]} по {(index + daysStep - qtySumDaysList[0])} {nameDaysList[1]}')

    # случай 2 = все в рамках месяца
    elif ((index-qtySumDaysList[(monthIn-1)]) < qtySumDaysList[monthIn]) and ((index + daysStep)-qtySumDaysList[(monthIn-1)]) < qtyDaysList[(monthIn-1)]:
        print("случай 2 = все в рамках месяца")
        print(
            f'Промежуток {type} темп = с {index-qtySumDaysList[monthIn-1]} {nameDaysList[monthIn]} по {((index+daysStep)-qtySumDaysList[(monthIn-1)])} {nameDaysList[monthIn]}')

    else:
        print("переход с месяца на месяц")
        startDay = index - qtySumDaysList[monthIn-1]
        startMonth = nameDaysList[monthIn-1]

        endDay = index + daysStep - qtySumDaysList[monthIn] + 1
        endMonth = nameDaysList[monthIn]

        print(
            f'Промежуток {type} темп = с {startDay} {startMonth} по {endDay} {endMonth}')


printIntervals(maxIndex, "max")
printIntervals(minIndex, "min")
