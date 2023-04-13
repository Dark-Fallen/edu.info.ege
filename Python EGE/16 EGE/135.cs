/**
Для решения задач 16 номера необходимо расписывать представленные в их условиях рекурсии. собственно, понимание рекурсия - половина
решения 16 номера.

Задача:
(А. Куканова) Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 1
F(n) = n · F(n – 1) – 1, если n > 1.
Чему равно значение выражения F(1000) / F(997)? В ответе укажите только целую часть числа.

Ответ: 997001999.
*/
using System;
using System.Numerics;

namespace Education
{
    static class Program
    {
        static void Main(string[] args)
        {
            BigInteger value1000 = 1;
            BigInteger value997 = 1;

            for (int i = 2; i < 1001; i++)
            {
                value1000 = value1000 * i - 1;
                if (i <= 997)
                    value997 = value997 * i - 1;
            }

            Console.WriteLine($"{value1000/value997}");
        }
    }
}