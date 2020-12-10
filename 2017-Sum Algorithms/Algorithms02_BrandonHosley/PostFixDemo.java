
public class PostFixDemo {
	
	public static void main(String[] Args) {
		
		/*
		 * change input data here.
		 */
		
		int data1 = 1;
		int data2 = 2;
		int data3 = 4;
		int data4 = 5;
		int data5 = 3;
		
		String postfix1 = data1 + " " + data2 + " + " + data3 + " * " + data4 + " - ";
		String postfix2 = data1 + " " + data2 + " * " + data3 + " " + data1 + " - / " + data4 + " " + data5 + " * + ";
		
		/*
		 * Print out the test data and results
		 */
	
		System.out.println("Test postfix solving algorithm:\n");
		
		System.out.println(postfix1 + "\nIs equal to:");
		System.out.println(Algorithm.evaluatePostFix(postfix1) + "\n"); //Should = 7
		
		System.out.println(postfix2 + "\nIs equal to:");
		System.out.println(Algorithm.evaluatePostFix(postfix2) + "\n"); //Should = 15
	}//end main

}
