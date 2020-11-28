/*
 * Brandon Hosley
 * 
 * Project Name: CSC372-CTA01-A
 * 
 * Project Purpose: This project is intended to be a proof of concept concerning certain features of Object Oriented Polymorphism.
 * 			Key concepts demonstrated will be superClasses, SubClasses, inheritance, and overriding methods.
 * 			This project is not intended to serve any purpose beyond proof of concept.
 * 
 * Algorithm Used: Inheritance used to demonstrate extending subclasses with features of superclasses
 * 
 * Inputs: Names (first and last), account number, withdrawal and deposit amounts.
 * 
 * Outputs: Will output account information and relevant data to specific account after actions changing the account are made.
 * 
 * Limitations:	Input data is ephemeral. Information used in the program is limited.
 * 
 * Errors:
 * 		First run: 	/n is not the same as \n in strings.
 * 		Second run: \b does not render in Eclipse but will run in Windows
 * 					overdraft visibility changed from private to protected
 * 
 * Added option to use user input to run tests, or to run the tests automatically with a method that will demonstrate several of the
 * specified use cases.
 * 
 * ==================
 */

import java.util.Scanner;

public class Test {
	public static void main (String Args[]) {
		//
		//TEST FILE
		//
		
		//hardcodeTest();
		userInputTest();
	}
	
	public static void userInputTest() {
		
		/*
		 * Test the account creation
		 */
		
		Scanner scnr = new Scanner(System.in);
		System.out.println("Please input first name:");
		String fName = scnr.nextLine();
		System.out.println("Please input last name:");
		String lName = scnr.nextLine();
		System.out.println("Please input test account ID:");
		int testID = scnr.nextInt(); scnr.nextLine();
		System.out.println("Please input test debit interest rate:");
		double testIntRate = scnr.nextDouble(); scnr.nextLine();
		
		BankAccount testBankAcct = new BankAccount(fName, lName, testID);
		CheckingAccount testDebitAcct = new CheckingAccount(fName, lName, testID, testIntRate);
		
		/*
		 * Test Bank account functionality
		 */
		
		System.out.println("Testing Summary...\n");
		testBankAcct.accountSummary();
		
		System.out.println("Please input test deposit:");
		int firstDep = scnr.nextInt(); scnr.nextLine();
		testBankAcct.deposit(firstDep);
		
		System.out.println("Please input test withdrawal:");
		int firstWith = scnr.nextInt(); scnr.nextLine();
		testBankAcct.withdrawal(firstWith);
		
		System.out.println("Testing Summary...\n");
		testBankAcct.accountSummary();
		
		
		/*
		 * Test Debit account functionality
		 */
		
		System.out.println("Testing Summary...\n");
		testDebitAcct.accountSummary();
		
		System.out.println("Please input test deposit:");
		int secondDep = scnr.nextInt(); scnr.nextLine();
		testDebitAcct.deposit(secondDep);
		
		System.out.println("Please input test withdrawal:");
		int secondWith = scnr.nextInt(); scnr.nextLine();
		testDebitAcct.withdrawal(secondWith);
		
		System.out.println("Testing Summary...\n");
		testDebitAcct.accountSummary();
		
		
		
		scnr.close();
		
	}
	
	public static void hardcodeTest() {
		//Test Regular Account
		
		BankAccount testBankAcct = new BankAccount("John", "Smith", 1337);
		
		testBankAcct.accountSummary();
		testBankAcct.deposit(100);
		testBankAcct.withdrawal(50);
		testBankAcct.withdrawal(100);
		testBankAcct.accountSummary();
		
		//Test Checking Account

		CheckingAccount testDebitAcct = new CheckingAccount("Jane", "Doe", 1234, 1.2);

		testDebitAcct.accountSummary();
		testDebitAcct.deposit(100);
		testDebitAcct.withdrawal(50);
		testDebitAcct.withdrawal(100);
		testDebitAcct.displayAccount();
	}
}
