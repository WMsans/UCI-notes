namespace Project_0A
{
    public static class Problem3
    {
        public static void Solution()
        {
            var name = Console.ReadLine();
            var age = Convert.ToInt32(Console.ReadLine());

            var unit = age == 1 ? "year" : "years";
            Console.WriteLine($"Your name is {name} and you are {age} {unit} old");
        }
    }
}
