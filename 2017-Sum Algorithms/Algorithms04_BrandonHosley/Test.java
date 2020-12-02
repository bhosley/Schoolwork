import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		
		int[] testArray = new int[] {2,8,5,4,1,3,7};
		
		System.out.println("Original array:  " + Arrays.toString(testArray));
		SortDemo.selectionSort(testArray);
		System.out.println("Final array:     " + Arrays.toString(testArray));
	}
}
