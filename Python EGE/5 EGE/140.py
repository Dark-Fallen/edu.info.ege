'''
Этапы решения задач 5 номера:
1. Определение функции, реализующей представленный в задаче алгоритм.
2. Реализация алгоритма перебора результата выполнения заданного значения для нахождения ответа.

Задача:
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописывается (дублируется) последняя цифра.
3) Затем справа дописывается бит чётности: 0, если в двоичном коде полученного числа чётное число единиц, и 1, если нечётное.
4) К полученному результату дописывается ещё один бит чётности.
Полученная таким образом запись (в ней на три разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
Укажите минимальное число R, большее 66, которое может быть получено в результате работы этого алгоритма. 
В ответе это число запишите в десятичной системе.

Ответ: 78.
'''

# Решение задачи

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
    binaryForm += binaryForm[len(binaryForm) - 1]
    count_of_units: int = 0
    for i in binaryForm:
        if i == '1':
            count_of_units += 1
    if count_of_units % 2 == 0:
        binaryForm += '00'
    else:
        binaryForm += '10'
    return fromBinary(binaryForm)

n: int = 1
while Algorythm(n) <= 66:
    n += 1

print(Algorythm(n))



