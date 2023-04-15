'''
Решение задач 25 номера ранних версий представляло собой перебор больших промежутков и поиск среди них чисел, удовлетворяющих
заданным условиям. Зачастую условием было наличие определенного количества четных/нечетных или кратных/некратных
определенному числу делителей. Без оптимизации такие задачи не решались.

Новые задачи подразумевают перебор значений в промежутке по заданной маске (пример маски: '123*456?7890') и проверка по различным
условиям задач.

Задача:
(А. Кабанов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425. Среди натуральных чисел, не превышающих 109, найдите все числа,
соответствующие маске 1?34567?9 и делящиеся на 17 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в
порядке возрастания, а во втором столбце — соответствующие им частные от деления на 17.

Ответ: 113456759 6673927
       133456749 7850397
       153456739 9026867
       173456729 10203337
       193456719 11379807.
'''

import itertools

for x, y in itertools.product(range(10), range(10)):
    value = int(f'1{x}34567{y}9')
    if value % 17 == 0:
        print(f'Новая пара чисел: {value} {value // 17}')
