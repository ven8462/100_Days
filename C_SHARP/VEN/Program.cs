namespace Program;
//Console.WriteLine("Hello, World!");
//Console.WriteLine(55);
//Console.WriteLine(55.6);
//string Name = "Lavender";
//int Age = 22;
//Console.WriteLine($"My name is {Name} and I'm {Age} yrs old");
//Console.WriteLine("I hope {Name} will figure out her life");

//Console.Write("Enter your name: ");
//string name = Console.ReadLine();
//Console.WriteLine($"Hello {name}");

//Console.Write("Enter number: ");
//string input = Console.ReadLine();
//Console.WriteLine(input);
//int num = int.Parse(input);
//Console.WriteLine(num);

// INPUT and CONVERSION
//Console.Write("Enter number: ");
//int num = Convert.ToInt32(Console.ReadLine());
//Console.WriteLine(num * 2);

// ARRAYS
//int[] IntArray = {1, 2, 3, 5};
//string[] StringArray = {"Hello", "Lavender", "Ven", "Akida"};
//Console.WriteLine(IntArray[2]);
//Console.WriteLine(StringArray[2]);

// METHODS


class Program
{
    static void Main(string[] args)
    {
        //GetInfo();
        //Console.WriteLine("Hello Lavender");
        //SayHi("Mike", 33);

        Book Deus = new Book();
        Deus.title = "Homo";
        Deus.Author = "Lavender";
        Deus.num_pages = 44;

        Book book2 = new Book();
        book2.title = "SOLD";
        book2.Author = "Ven";
        book2.num_pages = 400;

        Console.WriteLine(book2.title.ToLower());
        Console.WriteLine(Deus.title.ToUpper());

        Student student = new Student("Ven", "SE", 7);
        Console.WriteLine(student.Passed());
    }

    

  /* static void GetInfo()
    {
        Console.Write("Enter name: ");
        string name = Console.ReadLine();
    }

    static void SayHi(string name, int age)
    {
        Console.WriteLine("Hello " + name + "you are " + age);
    }
    */
}