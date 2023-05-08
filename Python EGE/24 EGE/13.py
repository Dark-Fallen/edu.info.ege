'''
Для решения задач 24 номера важно уметь обрабатывать строки наиболее 
эффективным способом.

Задача:
В текстовом файле k7-75.txt находится цепочка из символов латинского алфавита A,
B, C. Найдите длину самой длинной подцепочки, состоящей из символов C.

Ответ: 19.
'''

f = open('k7-75.txt', 'r')
data = f.read()
maxLen = 0
currentLen = 0
for i in data:
    if i == 'C':
        currentLen += 1
    else:
        if currentLen > maxLen:
            maxLen = currentLen
        currentLen = 0

print(maxLen)
