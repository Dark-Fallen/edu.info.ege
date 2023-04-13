'''
Для решения задач 17 номера нужно уметь считывать данные из файла. Также нужно уметь обрабатыввать значения последовательностей
попарно (по тройкам, четверкам и т. д.):
a) Когда парой (тройкой, четверкой и т. д.) считаются только идущие подряд числа.
b) Когда парой (тройкой, четверкой и т. д.) считаются не обязательно идущие подряд числа.

Задача:
(Е. Джобс) В файле 17-332.txt содержится последовательность целых чисел. Элементы последовательности – четырёхзначные натуральные числа.
Найдите все тройки элементов последовательности, в которых первое и последнее число тройки имеют одинаковую сумму цифр, а среднее число
тройки меньше, чем среднее арифметическое всех чисел в файле, кратных 17. В ответе запишите количество найденных троек, затем самую
часто встречающуюся сумму разрядов среди средних чисел таких троек. В данной задаче под тройкой подразумевается три идущих подряд
элемента последовательности.

Ответ: 257 19.
'''

file = open('17-332.txt', 'r')

nums = [int(i) for i in file.readlines() if i != '']

sNums = [i for i in nums if i % 17 == 0]
aMean = sum(sNums)/len(sNums)

digitsSums = [0 for i in range(36)]

count = 0

for i in range(len(nums) - 2):
    firstNum = nums[i]
    secondNum = nums[i + 1]
    thirdNum = nums[i + 2]
    digitsSum1 = firstNum % 10 + firstNum // 10 % 10 + firstNum // 100 % 10 + firstNum // 1000
    digitsSum3 = thirdNum % 10 + thirdNum // 10 % 10 + thirdNum // 100 % 10 + thirdNum // 1000
    if (digitsSum1 == digitsSum3 and secondNum < aMean):
        count += 1
        digitsSums[secondNum % 10 + secondNum // 10 % 10 + secondNum // 100 % 10 + secondNum // 1000] += 1

print(f'Число троек: {count}. Наиболее часто поввторяемая сумма: {digitsSums.index(max(digitsSums))}')

