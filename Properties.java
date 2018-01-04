import java.util.*;
import java.io.*;

/**
 * The propertie class is the class that represents all the properties and their values that have been detected in the text.
 *
 * @author (Paul JEAN)
 * @version (0.1)
 */
public class Properties
{
    private String value;
    private ArrayList<String> listOfValues; // List of all the values associated to each properties
    private String name; 
    /**
     * Constructor for objects of class Propertie
     */
    public Properties(String newName)
    {
        name = newName; 
        listOfValues= new ArrayList<String>();
        value= null;
        
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void setList( ArrayList myList)
    {
       Scanner sc = new Scanner(System.in);
       Scanner sv = new Scanner (System.in);
       boolean b = false; 
       
       while (b==false){
         System.out.println("Type a potential value");  
         String value = sc.nextLine();
         myList.add(value);
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
    public void setListOfValue(){
    setList(listOfValues);
    }
    
    public void displayList(){ 
       for (int i=0; i < listOfValues.size();i++){
           String s = listOfValues.get(i);
           System.out.println(s);}
    }
    
    public String getName(){
        return name;
    }
    
    public ArrayList getListOfValues(){
    return listOfValues;
    }
    
    public String getValue (){
    return value;
    }
    
    public void setValue (String newValue){
    value=newValue;
    }
    
    //public void researchValue (String text);
    }
