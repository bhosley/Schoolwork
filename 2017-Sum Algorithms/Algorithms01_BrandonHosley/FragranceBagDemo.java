/*
 * Brandon Hosley
 * 
 * Project Name: CSC400
 * 
 * Project Purpose: Use the ADT Bag to implement a container that functions similar to an array with similar methods.
 * 
 * Algorithm Used: Bag ADT.
 * 
 * Inputs: None, test class will make it happen.
 * 
 * Outputs: Confirmation of test actions and proof of proper output.
 * 
 * Limitations: The class is implemented with a test and no non-trivial application at this time.
 * 
 * Errors:
 * 
 * ==================
 */

public class FragranceBagDemo {
	
	public static void main(String[] args) {
		Fragrance frankincense = new Fragrance("Frankincense", 20);
		Fragrance rosebud = new Fragrance("Rosey", 200);
		Fragrance bodyOdor = new Fragrance("Sweaty", 1);
		Fragrance oldSpice = new Fragrance("Spicey", 25);
		Fragrance lavender = new Fragrance("Lavender", 50);
		Fragrance[] demoContents = new Fragrance[] {
				frankincense, rosebud, bodyOdor, oldSpice, lavender};

		FragranceBag<Fragrance> demoBag = new FragranceBag<Fragrance>();
		
		displayBag(demoBag);
		testAdd(demoBag, demoContents);
	}
	
	private static void testAdd(FragranceBag<Fragrance> bag, Fragrance[] content) {
		System.out.println("Attempting to add items to bag...");
		for (int i = 0; i< content.length; i++) {
			bag.add(content[i]);
		}
		System.out.println();
		displayBag(bag);
	}
	
	private static void displayBag(FragranceBag<Fragrance> bag) {
		System.out.println("Attempting to print contents of Bag:\n\n");
		Object[] contentArray = bag.toArray();
		for (int i=0; i<contentArray.length; i++) {
			System.out.println(((Fragrance) contentArray[i]).smell());
		}
		System.out.println();
	}
}
