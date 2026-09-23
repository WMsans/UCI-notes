namespace Project_0A
{
    public static class Problem2
    {
        private static string Concatenate(string str1, string str2)
        {
            return string.Concat(str1, str2);
        }

        public static void Solution()
        {
            var str1 = Console.ReadLine();
            var str2 = Console.ReadLine();

            if (str1 == null) return;
            if (str2 == null) return;
            var ans = Concatenate(str1, str2);
            Console.WriteLine(ans);
        }
    }
}