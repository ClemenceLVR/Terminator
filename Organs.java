import java.util.*;
import java.io.*;
/**
 * This class determines the structure of an organ.
 *
 * @author (Aurelia Leon)
 * @version (V0.1)
 */
public abstract class Organs
{
    private ArrayList<String> listOfOrgans;
    private String name;
    
    /**
     * Constructor for objects of class Organs
     */
    public Organs(String newName)
    {
        name = newName;
        listOfOrgans = new ArrayList<String>();
    }
    public void setListOfOrgans()
    {
        listOfOrgans.add(name);
    }
    public String getName()
    {
        return name;
    }
    public ArrayList getListOfOrgans()
    {
        return listOfOrgans;
    }
}
