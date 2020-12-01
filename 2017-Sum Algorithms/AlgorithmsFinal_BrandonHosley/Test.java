
public class Test {
	public static void main (String[] Args) {
		PersonQueue line = new PersonQueue();
		Person person1 = new Person("Michael", "Scott", 99);
		Person person2 = new Person("Dwight","Schrute",36);
		Person person3 = new Person("James","Halpert",26);
		Person person4 = new Person("Pamela","Beasley", 25);
		Person person5 = new Person("Stanley","Hudson",58);
		Person person6 = new Person("Angela","Martin",31);
		Person person7 = new Person("Andrew","Bernard",32);
		Person person8 = new Person("Kevin","Malone",44);
		
		System.out.println("Printing initial - Should be empty...");
		print(line);
		
		System.out.println("\nAdding two people...");
		line.add(person1);
		line.add(person2);
		print(line);
		
		System.out.println("\nAdding the remaining 6 people...");
		line.add(person3);
		line.add(person4);
		line.add(person5);
		line.add(person6);
		line.add(person7);
		line.add(person8);
		print(line);
		
		System.out.println("\nTest after removing the first four people...");
		line.remove(); line.remove(); line.remove(); line.remove();
		print(line);
		
		System.out.println("\nPutting everyone back into line...");
		line.add(person1);
		line.add(person2);
		line.add(person3);
		line.add(person4);
		print(line);
		
		System.out.println("\nTesting sorting by age...");
		line.sortByAge();
		print(line);
		
		System.out.println("\nTesting sorting by last name...");
		line.sortByLastName();
		print(line);
		
		System.out.println("\nTesting sorting by first name...");
		line.sortByFirstName();
		print(line);
		
		/*
		System.out.println("\n");
		print(line);
		*/
	}
	
	private static void print(PersonQueue someLine) {
		PersonQueue newLine = new PersonQueue(someLine);
		while (!newLine.isEmpty()) {
			newLine.remove().printInfo();
		}
		System.out.println();
	}
	
}
