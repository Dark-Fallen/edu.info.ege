'''
Для решения задач 24 номера важно уметь обрабатывать строки наиболее 
эффективным способом. Также важно помнить, что строки - массивы символов.

Задача:
Текстовый файл 24-211.txt содержит строку из набора A, B, C, D, E, F, всего не 
более чем из 106 символов. Найдите максимальное количество подряд идущих четвёрок 
символов ABEC, BDAC, CAFB, CFBA, стоящих одна за другой и пересекающихся с 
соседними четвёрками одной буквой. Например, в строке BDEABECAFBDACBD такие пары 
составляют подстроку ABECAFBDAC = ABEC + СAFB + ВDAC, итого 3 четвёрки.

Ответ: 81.
'''

data = open('24-211.txt', 'r').read()
subStrs = ['ABEC', 'BDAC', 'CAFB', 'CFBA']

maxLine = ''
currentLine = ''

i = 0
while i < len(data) - 3:
    if data[i] + data[i + 1] + data[i + 2] + data[i + 3] in subStrs:
        if currentLine == '':
            currentLine += data[i] + data[i + 1] + data[i + 2] + data[i + 3]
        else:
            currentLine += data[i + 1] + data[i + 2] + data[i + 3]
        i += 3
    else:
        if len(currentLine) > len(maxLine):
            maxLine = currentLine
        currentLine = ''
        i += 1

print((len(maxLine) - 1) / 3)
