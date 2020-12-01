
public class Person {
	String firstName, lastName;
	int age;
	
	public Person(String fName, String lName, int ageEntry) {
		firstName = fName;
		lastName = lName;
		age = ageEntry;
	}
	
	public void printInfo() {
		System.out.printf("%s %s %d%n", firstName, lastName, age);
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public int getAge() {
		return age;
	}
}
