// Brandon Hosley
// CSC320 - Programming 1
// 2018 01 25

import java.util.Scanner;

public class StringReversal {
	public static String ReverseOrder (String string1, String string2, String string3) {
		return (string3 + " " + string2 + " " + string1);
	};
	
	public static String ReverseLetters (String string1, String string2, String string3) {
		return (
				new StringBuilder(string1).reverse().toString() + " " +
				new StringBuilder(string2).reverse().toString() + " " +
				new StringBuilder(string3).reverse().toString() + " "
				);			
	};
	
	public static void main (String args[]) {
		Scanner scnr = new Scanner(System.in); 
		String string1, string2, string3;
		
		System.out.println("Please enter first word.");
		string1 = scnr.nextLine();
		System.out.println("Please enter second word.");
		string2 = scnr.nextLine();
		System.out.println("Please enter third word.");
		string3 = scnr.nextLine();
		
		System.out.println("The results of this reversal are: ");
		System.out.println(ReverseOrder (string1, string2, string3));
		System.out.println(ReverseLetters (string1, string2, string3));
	};
}
