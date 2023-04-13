'''
Для решения задач 16 номера необходимо расписывать представленные в их условиях рекурсии. собственно, понимание рекурсия - половина
решения 16 номера.

Задача:
(Е. Джобс) Алгоритм вычисления функции F(n), где n – целое число, задан следующими соотношениями:
F(n) = 1, если n < 3
F(n) = F(n – 2) – F(n – 1), если n > 2 и число n чётное,
F(n) = F(n – 2) – F(n – 3) , если n > 2 и число n нечётное.
Вычислите значение F(50).

Ответ: 8388608.
'''

# Решение задачи

def F(n: int) -> int:
    if n < 3: return 1
    elif n % 2 == 0: return F(n - 2) - F(n - 1)
    else: return F(n - 2) - F(n - 3)

print(F(50))