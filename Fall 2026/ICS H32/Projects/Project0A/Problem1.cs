namespace Project_0A
{
    public static class Problem1
    {
        private static double Perimeter(double width, double height)
        {
            var c = Math.Pow(width, 2)  + Math.Pow(height, 2);
            return Math.Sqrt(c) + width + height;
        }

        public static void Solution()
        {
            var width = Convert.ToDouble(Console.ReadLine());
            var height = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine(Problem1.Perimeter(width, height));
        }
    }
}