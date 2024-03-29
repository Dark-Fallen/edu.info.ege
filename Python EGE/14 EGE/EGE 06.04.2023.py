'''
Для решения обновленных задач 14 номера необходимо использовать алгоритм перебора значений переменных x, y, z, ...,
за которыми скрываются цифры с некоторых системах счисления, для проверки всевозможных комбинаций значений на соответствие поставленным
условиям.

Задача:
Операнды арифметического выражения записаны в системе счисления с основанием 15.
97968x21₁₅ + 7x23₁₅
В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления. Определите наибольшее значение x,
при котором значение данного арифметического выражения кратно 14. Для найденного значения x вычислите частное от
деления значения арифметического выражения на 14 и укажите его в ответе в десятичной системе счисления.
Основание системы счисления в ответе указывать не нужно.

Ответ: 116047226.
'''

for x in range(15):
    value1 = 9 * 15 ** 7 + 7 * 15 ** 6 + 9 * 15 ** 5 + 6 * 15 ** 4 + 8 * 15 ** 3 + x * 15 ** 2 + 2 * 15 + 1
    value2 = 7 * 15 ** 3 + x * 15 ** 2 + 2 * 15 + 3

    if (value1 + value2) % 14 == 0:
        print(f'Значение x, для которого выражение кратно 14: {x}. Частное от деления значения выражения на 14: {(value1 + value2) / 14}.')