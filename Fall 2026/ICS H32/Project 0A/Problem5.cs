namespace Project_0A
{
    public static class Problem5
    {
        private static string LongestString(List<string> list)
        {
            var  longest = "";
            foreach (var s in list)
            {
                if(s.Length > longest.Length) longest = s;
            }
            return longest;
        }

        public static void Solution()
        {
            var list = new List<string>
            {
                "apple",
                "banana",
                "kiwi"
            };

            Console.WriteLine(LongestString(list));
        }
    }
}
