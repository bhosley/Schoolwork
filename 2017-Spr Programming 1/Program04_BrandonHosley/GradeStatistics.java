// Brandon Hosley
// CSC320 - Programming 1
// 2018 01 25

import java.util.Scanner;
import java.util.Arrays;

public class GradeStatistics {
	public static void main(String args[]) {
		double[] grades;
		grades = new double[5];
		Scanner scnr = new Scanner(System.in);
		
		for(int i=0; i<5; i++) {	
			String cardinal = "";
			switch (i) {
			case 0: cardinal = "first"; break;
			case 1: cardinal = "second"; break;
			case 2: cardinal = "third"; break;
			case 3: cardinal = "fourth"; break;
			case 4: cardinal = "fifth"; break;
			default: break;
			};
			
			System.out.println("Please enter " +cardinal+ " grade.");
			grades[i] = scnr.nextDouble();	
		};
		
		Arrays.sort(grades);
		double sum = 0;
		for(double i : grades) {
			sum += i;
		};
		double average = sum / grades.length;
		
		System.out.println("The lowest grade is: " + grades[0]);
		System.out.println("The highest grade is: " + grades[grades.length - 1]);
		System.out.println("The average of grades is: " + average);
		
		scnr.close();		
	}
}
