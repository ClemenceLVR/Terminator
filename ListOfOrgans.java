import java.util.ArrayList;

/** 
 * Class list of organs 
 * Gathers all the organs that have been found in the text
 * 
 * @author clemence
 * @version 1/12/17
 */
public class ListOfOrgans {

	private ArrayList<Organs> organsList;
	private ArrayList<Organs> organsFoundList;
	private String nameList;
	
	/** 
	 * Constructor of the class ListOfOrgans
	 */
	public ListOfOrgans () {
		
	}
	
	/**
	 * Method allowing the user to get the organsList array
	 * @return organsList array
	 */
	public ArrayList getOrgansList() {
		return organsList;
	}
	
	/**
	 * Method allowing the user to set the organsList array
	 */
	public void setOrgansList() {
		
	}
	
	/**
	 * Method allowing the user to get the name of the list
	 * @return
	 */
	public String getName() {
		return nameList;
	}
	
	/**
	 * Method allowing the user to get the list of the organs founded in the text
	 * @return organsFoundList
	 */
	public ArrayList getOrgansFoundList () {
		return organsFoundList;
	}
	
	/**
	 * Method allowing the user to set the list of the organs founded in the text 
	 */
	public void setOrgansFoundList () {
		
	}
}
