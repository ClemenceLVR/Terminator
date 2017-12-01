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
    private static ArrayList<String> possibleProperties;
    private ArrayList<Properties> foundedProperties; 
    private String name;
    
    /**
     * Constructor for objects of class ListOfPropertie
     */
    public ListOfPropertie(String newName)
    {
        name= newName;
        foundedProperties= new ArrayList<Properties>();
    }

    /**
     * Method allowing the user to get the array of the possible properties
     * @return possibleProperties array
     */
    public ArrayList getPossibleProperties () {
    	return possibleProperties;
    }
    
    /**
     * Method allowing the user to get the array of the founded properties
     * @return foundedProperties array
     */
    public ArrayList getFoudedProperties () {
    	return foundedProperties;
    }
    
    /**
     * Method allowing the user to set the possible properties array
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
    
    /**
     * Method allowing the user to set the founded properties array
     */
    public void setFoundedProperties () {
    	
    }
}
