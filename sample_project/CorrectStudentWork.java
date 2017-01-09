
/**
 * Write a description of class CorrectStudentWork here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class CorrectStudentWork
{
    private static SolutionClass key = new SolutionClass();
    private static SumClass stu = new SumClass();
    

    /**
     * Constructor for objects of class CorrectStudentWork
     */
    public static void main (String[] args)
    {
        int points = 0; 
        System.out.println("Total items checked: 1");
         if (key.getSum(3,5)==stu.getSum(3,5))
         {
            points ++;
         }
         
         System.out.println("Points earned: " + points);
         
         
    }

}
