'''
Этапы решения задач 5 номера:
1. Определение функции, реализующей представленный в задаче алгоритм.
2. Реализация алгоритма перебора результата выполнения заданного значения для нахождения ответа.

Задача:
(Е. Джобс) Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) К этой записи дописываются разряды по следующему правилу: если единиц больше, чем нулей, в конец
приписывается 0, иначе в начало строки приписывается две единицы.
3) Пункт 2 повторяется ещё один раз.
Полученная таким образом запись является двоичной записью искомого числа R. Укажите минимальное число N,
при вводе которого получится значение R больше, чем 500. В ответе запишите это число в десятичной системе.

Ответ: 32.
'''

def toBinary(number: int) -> str:
    res: str = ''
    while number > 0:
        res += str(number % 2)
        number //= 2
    return res[::-1]

def fromBinary(binaryNumber: str) -> int:
    res: int = 0
    reversed_binary: str = binaryNumber[::-1]
    for i in range(len(reversed_binary)):
        res += int(reversed_binary[i]) * pow(2, i)
    return res

def Algorythm(N: int) -> int:
    binaryForm: str = toBinary(N)
    if (binaryForm.count('1') > binaryForm.count('0')):
        binaryForm += '0'
    else:
        binaryForm = '11' + binaryForm
    if (binaryForm.count('1') > binaryForm.count('0')):
        binaryForm += '0'
    else:
        binaryForm = '11' + binaryForm
    return fromBinary(binaryForm)

N: int = 1

while Algorythm(N) <= 500:
    N += 1

print(f'Наименьшее значение N: {N}. Результат R: {Algorythm(N)}.')