
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class SubsetTarget {
	public static void main(String args[]) {
		LinkedIntegerList numList = new LinkedIntegerList();
		try { numList = loadItems(); } catch (IOException e) { e.printStackTrace(); }
		if ( numList.size() > 0 ) {
			if(enumerateAndCheckSubsets(numList)) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		} else {
			System.out.println("Unable to Parse List.");
		}
	}
	
	private static boolean enumerateAndCheckSubsets(LinkedIntegerList input) {
		Boolean result = false;
		outerloop:
		for(int k = ( input.size() / 2 ); k > 0; k--) {
			int[] indices = new int[k];					// indices 
			if (k <= input.size() ) {					// first index sequence: 0, 1, 2, ...
			    for (int i = 0; (indices[i] = i) < k - 1; i++);
			    
			    LinkedIntegerList tempA = new LinkedIntegerList();
			    LinkedIntegerList tempB = new LinkedIntegerList();
			    makeSubsets(indices, tempA, tempB, input);
			    if( CheckSubset(tempA, tempB ) ) {
			    	result = true;
			    	break;	
			    }
			    
			    for(;;) {
			        int i;
			        // find position of item that can be incremented
			        for (i = k - 1; i >= 0 && indices[i] == input.size() - k + i; i--); 
			        if (i < 0) {
			            break;
			        }
			        indices[i]++;                    // increment this item
			        for (++i; i < k; i++) {    // fill up remaining items
			        	indices[i] = indices[i - 1] + 1; 
			        }
				    LinkedIntegerList tempC = new LinkedIntegerList();
				    LinkedIntegerList tempD = new LinkedIntegerList();
				    makeSubsets(indices, tempC, tempD, input);
				    if( CheckSubset(tempC, tempD ) ) {
				    	result = true;
				    	break outerloop;
				    }  
			    }
			}
		}
		return result;
	}
	
	public static void makeSubsets(int[] aIndeces, LinkedIntegerList subsetA, LinkedIntegerList subsetB, LinkedIntegerList wholeList) {
		for (int i = 0, j = 0; i < wholeList.size(); i ++) {
			if (j < aIndeces.length && aIndeces[j] == i) {
				subsetA.add(wholeList.get(i));
				j++;
			} else {
				subsetB.add(wholeList.get(i));
			}
		}
	}

	private static Boolean CheckSubset(LinkedIntegerList subset1, LinkedIntegerList subset2) {
		Boolean result = false;
		int sum1 = listSum(subset1);
		int sum2 = listSum(subset2);
		
		testPrint(subset1);
		System.out.print("( " + sum1 + " )        ");
		testPrint(subset2);
		System.out.print("( " + sum2 + " )");
		System.out.println();
		
		if(subset1.contains(sum2) && subset2.contains(sum1)) {
			result = true;
		}
		return result;
	}
	
	private static void testPrint(LinkedIntegerList list) {
		for (int i = 0; i < list.size(); i++) 
		{ 
		    System.out.print(list.get(i) + " ");
		}
	}
	
	private static int listSum(LinkedIntegerList l) {
		int total = 0;
		for(int i = 0; i < l.size(); i++) {
			total += l.get(i);
		}
		return total;
	}
	
	private static LinkedIntegerList loadItems() throws IOException {
		Path filePath = Paths.get("in.txt");
		Scanner scanner = new Scanner(filePath);
		LinkedIntegerList integers = new LinkedIntegerList();
		while (scanner.hasNext()) {
		    if (scanner.hasNextInt()) {
		        integers.add(scanner.nextInt());
		    } else {
		        scanner.next();
		    }
		}
		scanner.close();
		return integers;
	}
}
