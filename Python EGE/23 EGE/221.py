'''
Для решения задач 23 номера наиболее эффективным способом важно уметь решать 16 номера при помощи рекурсий, поскольку их реализация
позволяет формально выстроить древо всевозможных вариаций, которые необходимо искать в 23 номере.

Задча:
(Е. Джобс) Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Прибавь 2
3. Умножь на 2
Первая команда увеличивает число на 1, вторая – на 2, третья – вдвое. Программа для исполнителя – это последовательность команд.
Сколько существует таких программ, которые исходное число 3 преобразуют в число 25 и при этом в программе есть все три команды?

Ответ: 15092.
'''

count: int = 0

def F(n: int, has1: bool, has2: bool, has3: bool) -> None:
    global count

    if n >= 25:
        if n == 25 and has1 and has2 and has3:
            count += 1
        return
    F(n + 1, True, has2, has3)
    F(n + 2, has1, True, has3)
    F(n * 2, has1, has2, True)

F(3, False, False, False)
print(count)

