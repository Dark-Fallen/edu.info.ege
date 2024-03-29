'''
Для решения задач 23 номера наиболее эффективным способом важно уметь решать 16 номера при помощи рекурсий, поскольку их реализация
позволяет формально выстроить древо всевозможных вариаций, которые необходимо искать в 23 номере.

Задча:
Исполнитель преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавь 2
2. Припиши 2
Первая команда увеличивает число на экране на 2, вторая приписывает 2 в конец десятичной записи числа. Программа для исполнителя –
это последовательность команд. Например, если в начальный момент на экране находится число 1, то программа 212 последовательно
преобразует его в 12, 14, 142. Сколько существует различных программ, которые преобразуют исходное число 2 в число 900?

Ответ: 121.
'''

count: int = 0

def F(n: int) -> None:
    global count

    if n > 900:
        return
    elif n == 900:
        count += 1
        return
    F(n + 2)        # 1. Прибавь 2
    F(n * 10 + 2)   # 2. Припиши 2

F(2)
print(count)