'''
Для решения задач 23 номера наиболее эффективным способом важно уметь решать 16 номера при помощи рекурсий, поскольку их реализация
позволяет формально выстроить древо всевозможных вариаций, которые необходимо искать в 23 номере.

Задча:
(ЕГЭ-2022) Исполнитель преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
1. Вычти 1
2. Найди целую часть от деления на 2
Первая команда уменьшает число на экране на 1, вторая заменяет число на экране на целую часть от деления числа на 2.
Сколько существует программ, для которых при исходном числе 30 результатом является число 1, и при этом траектория вычислений
содержит число 12?

Ответ: 376.
'''

count = 0

def F(n: int, has12: bool) -> None:

    global count

    if n == 1:
        count += 1 if has12 else 0
        return
    
    if n < 12 and not(has12):
        return
    
    if n == 12:
        has12 = True
        
    F(n - 1, has12)
    F(n // 2, has12)

F(30, False)
print(count)