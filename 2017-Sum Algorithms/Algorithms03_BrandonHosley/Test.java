import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		
		int[][] testSet = new int[][] {
			{1,2,3,4,5},
			{1,2,3},
			{1,3,5,7,9},
			{0,0,1,2,3},
			{0,0,0,0,0,0,0,0,1,0,0,0,2,0,0},
			{123456789,0},
			{},
			{,}
		};
		
		for (int i = 0; i < testSet.length; i++) {
			int[] testArray = testSet[i];
			
			System.out.println("The original Array is:    " + Arrays.toString(testArray));
			int[] testReverse = RecursionDemo.reverse(testArray);
			System.out.println("When reversed this is:    " + Arrays.toString(testReverse) + "\n");
		}//end for	
		
	}//end main
}


