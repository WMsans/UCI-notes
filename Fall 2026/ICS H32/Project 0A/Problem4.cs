namespace Project_0A
{
    public static class Problem4
    {
        private static double SumList(List<double> list)
        {
            var sum = 0.0;
            foreach (var number in list)
            {
                sum += number;
            }
            return sum;
        }

        public static void Solution()
        {
            var list = new List<double>
            {
                1,
                2,
                3
            };

            Console.WriteLine(SumList(list));
        }
    }
}