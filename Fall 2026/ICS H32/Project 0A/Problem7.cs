namespace Project_0A;

public class Problem7
{
    private static int CharacterLookupCount(string str, char c)
    {
        var count = 0;

        foreach (var ch in str)
        {
            if (ch == c) count++;
        }
        
        return count;
    }

    public static void Solution()
    {
        Console.Write("Please enter a string: ");
        var str = Console.ReadLine();
        Console.Write("Please enter a character: ");
        var c = Convert.ToChar(Console.ReadLine() ?? "");

        if (str != null) Console.Write(CharacterLookupCount(str, c));
    }
}