import java.util.ArrayList;

public class Sort {

	//Selection sort used to sort Alphabetically order (for demo purposes)
	
	public static ArrayList<String> alphabetical (ArrayList<String> list) {
		
		for(int i = 0; i < list.size(); i++) {
			String item = list.get(i);
			for(int j = i + 1; j < list.size(); j++) {
				if( CustomCompare.inOrder(item,list.get(j)) ) {
					String oldItem = item;
					String newItem = list.get(j);
					item = newItem;
					list.set(j, oldItem);
				}
			}
			list.set(i, item);
		}
		return list;
	}
	
	//Insertion sort used to sort Reversed order (for demo purposes)
	
	public static ArrayList<String> reverse (ArrayList<String> unsortedList) {
		ArrayList<String> sortedList = new ArrayList<String>();
		
		while(unsortedList.size() > 0) {
			int index = 0;
			String item = unsortedList.get(0);
			for(int i = 1; i < unsortedList.size(); i++) {
				if( !CustomCompare.inOrder(item,unsortedList.get(i)) ) {
					index = i;
					item = unsortedList.get(i);
				}
			}//end for
			unsortedList.remove(index);
			sortedList.add(item);
		}//end while
		
		return sortedList;
	}
	
	/* 
	  
	 ** The Selection Sort version of reverse ordered Sort. **
	
	 public static ArrayList<String> reverse (ArrayList<String> list) {
		
		for(int i = 0; i < list.size(); i++) {
			String item = list.get(i);
			for(int j = i + 1; j < list.size(); j++) {
				if( !CustomCompare.inOrder(item,list.get(j)) ) {
					String oldItem = item;
					String newItem = list.get(j);
					item = newItem;
					list.set(j, oldItem);
				}
			}
			list.set(i, item);
		}
		
		return list;
	} 
	
	** The Insertion version of Alphabetical ordered Sort. **
	
	public static ArrayList<String> alphabetical (ArrayList<String> unsortedList) {
		ArrayList<String> sortedList = new ArrayList<String>();
		
		while(unsortedList.size() > 0) {
			int index = 0;
			String item = unsortedList.get(0);
			for(int i = 1; i < unsortedList.size(); i++) {
				if( CustomCompare.inOrder(item,unsortedList.get(i)) ) {
					index = i;
					item = unsortedList.get(i);
				}
			}//end for
			unsortedList.remove(index);
			sortedList.add(item);
		}//end while
		
		return sortedList;
	}
	*/
	
}
