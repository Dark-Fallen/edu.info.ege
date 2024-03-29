'''
Для решения задач 24 номера важно уметь обрабатывать строки наиболее 
эффективным способом. Также важно помнить, что строки - массивы символов.

Задача:
Текстовый файл 24-1.txt содержит только заглавные буквы латинского алфавита 
(ABC…Z). Определите максимальное количество идущих подряд символов, среди 
которых буква A встречается не более пяти раз.

Ответ: 229.

Идея решения: выставляем левую границу в самом начале строки data, и считаем,
сколько раз встречается Aна нашем пути, параллельно сравнивая длины подстрок.
Как только находим 6 A в текущей подстроке, смещаем левую границу на позицию сразу после
первой найденной A, расположенной после левой границы.

Например, есть строка DSDDABBSABSAASSRFABABDJ. Левая граница будет на D(0). Прогоняем
цикл по строке, пока не найдем 6 A на позиции 19. После этого меняем левую границу на 5 и 
продолжаем прогон, пока опять не найдем 6 A или пока не дойдем до конца строки.
'''
f = open('24-1.txt', 'r')

data = f.read()

maxLen = 0
countOfA = 0

leftBound = 0

for i in range(len(data)):
    if data[i] == 'A':
        countOfA += 1
        if countOfA > 5:
            leftBound = data.find('A', leftBound) + 1
            countOfA = 5
    if i - leftBound + 1 > maxLen:
        maxLen = i - leftBound + 1

print(maxLen)
