'''
Решение задач 12 номера представляет собой реализацию алгоритма, представленного в них, на ЯП для дальнейшего его исполнения
при указанных входных данных.
Усложнены задачи могут быть лишь необходимостью перебора начальных входных данных.

Задача:
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов. 
заменить (v, w) 
нашлось (v) 
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, эта команда
не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. 
Дана программа для Редактора:

ПОКА нашлось (555) ИЛИ нашлось (888)
  заменить (555, 8)
  заменить (888, 55)
КОНЕЦ ПОКА

Известно, что начальная строка состоит более чем из 100 цифр 5 и не содержит других символов.
В ходе работы алгоритма получилась строка, не содержащая цифр 5. Укажите минимальную возможную длину входной строки.

Ответ: 101.
'''
# Задаем начальное число цифр 5 в строке, большее 100.
n: int = 101

while True:
    # Создаем строку из n цифр 5 и прогоняем по алгоритму из задачи
    line: str = '5' * n

    while line.find('555') > -1 or line.find('888') > -1:
        line = line.replace('555', '8', 1)
        line = line.replace('888', '55', 1)
    
    # Проверяем наличие цифр 5 в полученной строке. Если цифр 5 нет, выводим n и завершаем работу цикла
    if not('5' in line):
        print(n)
        print(line)
        break

    n += 1