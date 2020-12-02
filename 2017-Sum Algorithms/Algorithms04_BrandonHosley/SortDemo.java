import java.util.Arrays;

public class SortDemo {
	public static int[] selectionSort(int[] array) {
		for(int i=0; i<array.length; i++) {
			for(int j=i+1; j<array.length; j++) {
				
				int temp = array[i]; //holder variable, for switching out numbers
				
				//check for lower variables
				if (temp>array[j]) {
					temp = array[j];
					array[j] = array[i];
				}
				//set the on-deck item to the lowest value found during this pass
				array[i] = temp;
			}//end for	
			System.out.println("                 " + Arrays.toString(array));		
		}//end for
		return array;
	}//end selectionSort
}
