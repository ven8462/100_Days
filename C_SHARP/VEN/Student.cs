namespace Program;

public class Student
{
    public string name;
    public string major;
    public int gpa;


     public Student(string aName, string aMajor, int aGpa)
     {
        name = aName;
        major = aMajor;
        gpa = aGpa;
     }

     public bool Passed()
    {
        if(gpa >= 3)
        {
            return true;
        }
        return false;
    }
}