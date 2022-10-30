using System;

namespace Education
{
    class Program
    {

        static void Main(string[] args)
        {
            // Создаете алгоритм на основе методов replace(ref string, string, string) и firstEntrance(string, string)
        }

        static void replace(ref string line, string subline1, string subline2)
        {
            var index = firstEntrance(line, subline1);
            string new_line = "";
            for (var i = 0; i < index; i++)
            {
                new_line += line[i];
            }
            foreach (var t in subline2)
            {
                new_line += t;
            }

            for (var i = index + subline1.Length; i < line.Length; i++)
            {
                new_line += line[i];
            }

            line = new_line;
        }
        static int firstEntrance(string line, string substring)
        {
            for (var i = 0; i < line.Length; i++)
            {
                if (line.Length - i < substring.Length) break;
                if (line[i] != substring[0]) continue;
                var isSubString = true;
                for (var j = 1; j < substring.Length; j++)
                {
                    if (line[i + j] == substring[j]) continue;
                    isSubString = false;
                    i += + substring.Length;
                    break;
                }

                if (isSubString)
                {
                    return i;
                }
            }
            return -1;
        }
    }
}
