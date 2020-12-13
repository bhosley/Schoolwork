import java.io.PrintWriter;
import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String args[]) {
		
		ArrayList<Automobile> inventory = new ArrayList<Automobile>();
		boolean exitProgram = false;
		Scanner scanner = new Scanner(System.in);
		
		while (exitProgram == false) {
			String input = null;
			System.out.println("\nPlease choose one of the following options\nby typing the corresponding letter:");
			System.out.println("a: To add a new vehicle\n"
					+ "r: To remove a vehicle\n"
					+ "u: To update a vehicle\n"
					+ "i: To view the current inventory of vehicles\n"
					+ "s: To export a text file of the vehicles\n"
					+ "e: To exit the program");
			
			input = scanner.nextLine();
			
			switch (input) {
			case "a": addVehicle(inventory, scanner); break;
			case "r": removeVehicle(inventory, scanner); break;
			case "u": updateVehicle(inventory, scanner); break;
			case "i": showInventory(inventory); break;
			case "s": try{exportFile(inventory);}
						catch(IOException e) {System.out.println("Export has failed.");}; break;
			case "e": exitProgram = true; break;
			default: System.out.println("Please try again with a designated letter...\n"); break;
			};			
		};
		scanner.close();
		System.out.println("Thank you.\nExiting...");
		System.exit(0);
	};
	
	//
	//add a vehicle
	//
	
	public static void addVehicle(ArrayList<Automobile> arrayli, Scanner scnr) {
		
		System.out.println("What is the Make of the vehicle?");
		String make = scnr.nextLine();
		System.out.println("What is the Model of the vehicle?");
		String model = scnr.nextLine();
		System.out.println("What is the Color of the vehicle?");
		String color = scnr.nextLine();
		System.out.println("What is the Year of the vehicle?");
		int year = scnr.nextInt(); scnr.nextLine();
		System.out.println("What is the estimated Gas Mileage (MPG) of the vehicle?");
		int mileage = scnr.nextInt(); scnr.nextLine();
		
		Automobile newCar = new Automobile(make, model, color, year, mileage);
		arrayli.add(newCar);
		System.out.println("New Vehicle Added.\n");
	};
	
	//
	//show inventory
	//
	
	public static void showInventory(ArrayList<Automobile> arrayli) {
		int i = 0;
		while (i < arrayli.size()) {
			System.out.print(i + 1 + "   ");
			System.out.print(arrayli.get(i).getMake() + "   ");
			System.out.print(arrayli.get(i).getModel() + "   ");
			System.out.print(arrayli.get(i).getColor() + "   ");
			System.out.print(arrayli.get(i).getYear() + "   ");
			System.out.print(arrayli.get(i).getMileage() + "\n");
			i++;
		};
	};
	
	//
	//remove a vehicle
	//
	
	public static void removeVehicle(ArrayList<Automobile> arrayli, Scanner scnr) {
		//request user to state which vehicle to delete
		System.out.println("Please enter the index number for the vehicle\n"
				+ "you would like to remove from the inventory:");
		int index = scnr.nextInt(); scnr.nextLine();
		
		//If the index is valid delete the item,
		//otherwise exit method
		if (index <= arrayli.size()) {
			System.out.println("Removing vehicle number " + index +".");
			arrayli.remove(index-1);
		}else{
			System.out.println("Sorry, entry not recognized as valid...");
		};
	};
	
	//
	//update vehicle
	//
	
	public static void updateVehicle(ArrayList<Automobile> arrayli, Scanner scnr) {
		//request user to state which vehicle to update
		System.out.println("Please enter the index number for the vehicle\n"
				+ "that you would like to update:");
		int index = scnr.nextInt() - 1;scnr.nextLine();
		
		//If the index is valid have the user update each field manually the item,
		//otherwise exit method
		if (index <= arrayli.size()) {
			System.out.println("What is the new or current Make of the vehicle?");
			arrayli.get(index).updateMake(scnr.nextLine());
			System.out.println("What is the new or current Model of the vehicle?");
			arrayli.get(index).updateModel(scnr.nextLine());
			System.out.println("What is the new or current Color of the vehicle?");
			arrayli.get(index).updateColor(scnr.nextLine());
			System.out.println("What is the new or current Year of the vehicle?");
			arrayli.get(index).updateYear(scnr.nextInt()); scnr.nextLine();
			System.out.println("What is the new or current estimated Gas Mileage (MPG) of the vehicle?");
			arrayli.get(index).updateMileage(scnr.nextInt()); scnr.nextLine();
			
			//Automobile updatedCar = new Automobile(make, model, color, year, mileage);
			//arrayli.set(index, updatedCar);
		}else{
			System.out.println("Sorry, entry not recognized as valid...");
		};
	};
	
	//
	//export to an inventory file
	//
	
	public static void exportFile(ArrayList<Automobile> arrayli) throws IOException {
		
		File invFile = new File("inventory.txt");
		PrintWriter printer = new PrintWriter(invFile);
		printer.println("The current inventory of Automobiles:\n");
		
		int i = 0;
		while (i < arrayli.size()) {
			printer.print(i + 1 + "   ");
			printer.print(arrayli.get(i).getMake() + "   ");
			printer.print(arrayli.get(i).getModel() + "   ");
			printer.print(arrayli.get(i).getColor() + "   ");
			printer.print(arrayli.get(i).getYear() + "   ");
			printer.print(arrayli.get(i).getMileage() + "\n");
			i++;
		};
		printer.close();
		
		System.out.println("Export was successful.");
	};
}
