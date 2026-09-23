namespace Project_0A
{
    public class Problem8
    {
        private static bool IsPalindrome(string str)
        {
            for (var i = 0; i < str.Length / 2; i++)
            {
                if (str[i] != str[str.Length - 1 - i]) return false;
            }

            return true;
        }

        public static void Solution()
        {
            Console.Write("Please enter a string: ");
            var str = Console.ReadLine();

            if (str != null) Console.WriteLine(IsPalindrome(str));
        }
    }
}
