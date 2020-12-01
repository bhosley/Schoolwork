public class BankAccount {
	String firstName;
	String lastName;
	int accountID;
	double balance;
	
	//Constructor
	
	public BankAccount(String fName, String lName, int accID) {
		firstName = fName;
		lastName = lName;
		accountID = accID;
		balance = 0.0;
	}
	
	//
	//Object Methods
	//
	
	public void deposit(double depAmount) {
		try {
			balance = balance + depAmount;
			System.out.println(depAmount + " has been deposited.");
			System.out.println("The new balance is " + balance + "\n");
		} catch ( IllegalArgumentException e ) {
			System.out.println("Data entered should be a number.");
		}
	}
	
	public void withdrawal(double withAmount) {
		try {
			if (balance >= withAmount) {
			balance = balance - withAmount;
			System.out.println(withAmount + " has been withdrawn.");
			System.out.println("The new balance is " + balance + "\n");
			} else {
				overDraft(withAmount);
			}
		} catch ( IllegalArgumentException e ) {
			System.out.println("Data entered should be a number.");
		}
	}
		
	protected void overDraft(double withAmount) {
		System.out.println("Sorry, funds are insufficient for this withdrawal.\n");
	}
	
	public double getBalance() {
		return balance;
	}
	
	public void accountSummary() {
		System.out.println(
				"Account information for account " + accountID + ":\n" +
				"The owner of the account is " + firstName + lastName + "\n" +
				"The current balance of the account is: " + balance + "\n"
				);
	}
	
	//
	//Setters and Getters
	//
	
	public void setFirstName(String newFirstName) {
		firstName = newFirstName;
	}
	
	public void setLastName(String newLastName) {
		lastName = newLastName;
	}
	
	public void setAccountID(int newAccountID) {
		accountID = newAccountID;
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public int getAccountID() {
		return accountID;
	}
}
