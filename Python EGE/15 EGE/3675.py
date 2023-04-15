'''
Решение задач 15 номера при помощи программирования подразумевает перебор значений переменных для поиска наибольшего/наименьшего
значений для некоторого параметра A.

Задача:
(Е. Джобс) Для какого наименьшего целого неотрицательного числа А выражение
(x – 2y < 3A) ∨ (2y > x) ∨ (3x > 50)

тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y?

Ответ: 5.

Примечание: для ускоренного перебора можно провести оптимизацию по перебору для значений x, y в данной задаче.
'''

# Вариант ускоренного решения
for A in range(100):
    isMatchingNumber: bool = True
    for x in range(1, 50 // 3 + 1):
        for y in range(1, x // 2 + 1):
            if not(x - 2 * y < 3 * A):
                isMatchingNumber = False
                break
        if not(isMatchingNumber):
            break
    
    if (isMatchingNumber):
        print(f'Наименьшее значение параметра A: {A}.')
        break
# Вариант ускоренного решения


# Вариант Стандартного решения
for A in range(1, 1000):
    isMatchingNumber: bool = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x - 2*y < 3*A) or (2*y > x) or (3*x > 50)):
                isMatchingNumber = False
                break
        if not(isMatchingNumber):
            break
    
    if (isMatchingNumber):
        print(f'Наименьшее значение параметра A: {A}.')
        break
# Вариант Стандартного решения