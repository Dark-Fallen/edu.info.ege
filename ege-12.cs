// Для реализации функции заменить(v, w) можно использовать следующий пример

public static string MyReplaceMethod(this string root, string substring1, string substring2)
{
  root = root.Insert(root.IndexOf(substring1), substring2);
  root = root.Remove(root.IndexOf(substring1), substring1.Length);
  return root;
}

// Для реализации функции нашлось(v) достаточно использовать метод Contains()

/////////////////////////////// Пример использования
static void Main(string[] args)
{
  string val = new string('2', 10);     // val = "2222222222"
  val = val.MyReplaceMethod("22", "1"); // val = "122222222"
  Console.WriteLine(val);               // 122222222
  Console.ReadKey();
}
/////////////////////////////// Пример использования
