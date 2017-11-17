import java.util.*;
import java.io.*;
/**
 * This class is an extend of the property class. It allow to detect a propertie
 * relative to several organs (example position relative to)
 *
 * @author (Paul JEAN)
 * @version (0.1)
 */
public class PropertieRelative extends Propertie
{
    // instance variables - replace the example below with your own
    private static ArrayList<String> listOfIndicator;
    

    /**
     * Constructor for objects of class PropertieRelative
     */
    
    public PropertieRelative(String name){
    super(name);
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void  setIdentifier()
    {
        super.setList(listOfIndicator);
        
    }
}
