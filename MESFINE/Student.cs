namespace VEN// tie together files in the same project
{
     public class Student // create a class
     {
        // public attributes can be accessed outside the class
        public int Age {get; set;}
        public string Name {get; set;}
        public string Grade {get; set;}
        public int Id {get; set;}

        public string Print()
        {
            return $"The Student {Id}: age is {Age} their name is {Name} they have a grade of {Grade}";
        }
        
        public void Get_Info()
        {
            Console.WriteLine("Please enter the student age? ");
            Age = int.Parse(Console.ReadLine());

            Console.WriteLine("Please enter the student Name? ");
            Name = Console.ReadLine();

            Console.WriteLine("Please enter the student grade? ");
            Grade = Console.ReadLine();

            Console.WriteLine("Please enter the student id? ");
            Id = int.Parse(Console.ReadLine());
        }
     } 
}