using VEN;


namespace Cyril
{
    public class Teacher
    {
        public int Height { get; set;}
        public string Name {get; set;}

        public  List<Student> Students {get; set;}

        public void Teacher_Info()
        {
            Console.WriteLine("Enter Teachers Name? ");
            Name = Console.ReadLine();

            Console.WriteLine("Enter Teachers Height? ");
            Height = int.Parse(Console.ReadLine());

            Console.WriteLine("Please Enter the number of Students? ");
            int num = int.Parse(Console.ReadLine());

        Students = new List<Student>();

            for (int i = 0; i < num; i++)
            {
                Student anystudent = new Student();
                anystudent.Get_Info();
                Students.Add(anystudent);
            }

        }
        public void Print_Studentlist()
        {
            for (int j = 0; j < Students.Count; j++)
            {
                Console.WriteLine(Students[j].Print());
            }
        }

        public void Print_Teacherdetails()
        {
            Console.WriteLine($"The teacher's name is {Name} and the height is {Height}");
            Print_Studentlist();
        }
    }

}