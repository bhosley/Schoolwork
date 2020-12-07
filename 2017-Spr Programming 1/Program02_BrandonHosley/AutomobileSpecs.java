// Brandon Hosley
// CSC320 - Programming 1
// 2018 01 18

import java.util.Scanner;

public class AutomobileSpecs {
	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);
		String brand = "";
		String model = "";
		short year = 0;
		int startOdometer = 0;
		int endOdometer = 0;
		double estimatedMPG = 0.0; //was going to go with short but editor did not like
		
		System.out.println("What is the Brand of the vehicle?");
		brand = scnr.nextLine();
		System.out.println("What is the Model of the vehicle?");
		model = scnr.nextLine();
		System.out.println("What is the Year of the vehicle?");
		year = scnr.nextShort();
		System.out.println("What is the initial reading of the Odometer?");
		startOdometer = scnr.nextInt();
		System.out.println("What is the final reading of the Odometer?");
		endOdometer = scnr.nextInt();
		System.out.println("What is the estimated Gas Mileage (MPG) of the vehicle?");
		estimatedMPG = scnr.nextDouble();
		
		int distanceTravelled = (endOdometer - startOdometer);
		double fuelUsed = distanceTravelled / estimatedMPG;
		
		System.out.println("The vehicle described is a " + year + " " + brand + " " + model + ".");
		System.out.println("The vehicle was in use for " + distanceTravelled + " miles.");
		System.out.println("During that time it used approximately " + fuelUsed + " gallons of fuel.");
		
		scnr.close();
		return;
	}
}
