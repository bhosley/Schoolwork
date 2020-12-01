
public class CheckingAccount extends BankAccount {
	double interestRate;
	
	//Constructor 
	
	public CheckingAccount(String fName, String lName, int accID, double intRate) {
		super(fName, lName, accID);
		interestRate = intRate;
	}
	
	//Override overDraft() used in BankAccount.withdrawal()	
	@SuppressWarnings("unused")
	protected void overDraft(double withAmount) {
		this.balance = this.balance - withAmount - 30.0;
		System.out.println( withAmount + " has been withdrawn.\n" + 
				"Account has been overdrawn, $30 fee assessed.\n" +
				"The new account balance is: " + this.balance + "\n");
	}
	
	//
	//Object Methods
	//
	
	public void processWithdrawal(double withAmount){
		this.withdrawal(withAmount);
	}
	
	public void displayAccount() {
		this.accountSummary();
		System.out.println("\bThe current interest rate for this account is: " + 
		interestRate + " %APR.\n");
	}
	
	//
	//Getters and Setters
	//
	
	public void setInterestRate(double newIntRate) {
		interestRate = newIntRate;
	}
	
	public double getInterestRate() {
		return interestRate;
	}

}