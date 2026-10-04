namespace Project_0A
{
    public static class Problem6
    {
        private static bool IsUpper(char c)
        {
            return c >= 'A' && c <= 'Z';
        }

        private static bool IsValid(string license)
        {
            if (license.Length < 3) return false;
            if (!IsUpper(license[0]) || !IsUpper(license[^1])) return false;

            var hasDigit = false;
            for (var i = 1; i < license.Length - 1; i++)
            {
                var c = license[i];
                if (c >= '0' && c <= '9') hasDigit = true;
                else if (!IsUpper(c)) return false;
            }

            return hasDigit;
        }

        public static void Solution()
        {
            var license = Console.ReadLine();
            while (license == null || !IsValid(license))
            {
                license = Console.ReadLine();
            }
        }
    }
}
