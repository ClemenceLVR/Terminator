import java.util.*;
import java.io.*;
/**
 * This class group a list of the founded properties but also a list of all the
 *  possible properties .
 *
 * @author (Paul JEAN)
 * @version (0.1)
 */
public class ListOfPropertie
{
    // instance variables - replace the example below with your own
    private static ArrayList<String> possibleProperties;
    private ArrayList<Propertie> foundedProperties; 
    private String name;
    /**
     * Constructor for objects of class ListOfPropertie
     */
    public ListOfPropertie(String newName)
    {
        // initialise instance variables
        name= newName;
        foundedProperties= new ArrayList<Propertie>();
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void setPossibleProperties()
    {
        possibleProperties=new ArrayList<String>();
       Scanner sc = new Scanner(System.in);
       Scanner sv = new Scanner (System.in);
       boolean b = false; 
       
       while (b==false){
         System.out.println("Type a potential value");  
         String value = sc.nextLine();
         possibleProperties.add(value);
         System.out.println("vous avez saisi : "+value);
         System.out.println("Would you like to continue the type ?(Y/N)");
         String result= sv.nextLine();
         result= result.toUpperCase();
         switch(result){
            case "Y":
            value="";
            break;
            case "N":
            b= true;
            break;
            default:
            System.out.println("mauvaise saisie de choix recommencez");}
        }
    }
}
