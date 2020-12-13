// Brandon Hosley
// CSC320 - Programming 1
// 2018 01 25

import java.util.Scanner;
import java.text.DecimalFormat;

public class taxCalculator {
	public static void main(String [] args) {
		Scanner scnr = new Scanner(System.in);
		DecimalFormat df = new DecimalFormat("#.00"); 
		int income = 0;
		double taxRate = 0.0;
		double taxWithholding = 0.0;
		
		System.out.println("Please enter average weekly income:");
		income = scnr.nextInt();
		
		if (income < 500) {
			taxRate = 0.1;
		} else if ((income >= 500) && (income < 1500)) {
			taxRate = 0.15;
		} else if ((income >= 1500) && (income < 2500)) {
			taxRate = 0.2;
		} else {
			taxRate = 0.3;
		}
		
		taxWithholding = taxRate * income;		
		System.out.print("The weekly tax withholding for that amount will be $" + df.format(taxWithholding) + "." );
		
	}
}
