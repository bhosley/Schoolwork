import java.util.Comparator;

public class CustomCompare implements Comparator<String>{

	@Override
	public int compare(String s1, String s2) {
		return s1.compareTo(s2);
	}
	
	public static boolean inOrder(String s1, String s2) {
		if(s1.compareTo(s2)<0) {
			return false;
		} else {
			return true;
		}
	}
	
}
