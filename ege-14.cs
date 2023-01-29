// Реализация метода возведения в степень для типа BigInteger:

static BigIntager MyPow(int x, int y)
{
  BigInteger res = 1;
  for (int i = 0; i < y / 2; i++)
  {
    res *= x;
  }
  return y % 2 == 0 ? res * res : res * res * x;
}
