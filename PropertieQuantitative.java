import java.util.*;
import java.io.*;
/**
 * This class group the quantitative property wich cannot be indentified as size
 * lenght or heigt.
 *
 * @author (Paul JEAN)
 * @version (0.1)
 */
public class PropertieQuantitative extends Propertie
{
    // instance variables - replace the example below with your own
    private static ArrayList<String> listOfProp;

    /**
     * Constructor for objects of class PropertyQuantitative
     */
    public PropertieQuantitative(String name)
    {
        // initialise instance variables
        super(name);
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void setListOfProp ()
    {
       super.setList(listOfProp);
    }
}
