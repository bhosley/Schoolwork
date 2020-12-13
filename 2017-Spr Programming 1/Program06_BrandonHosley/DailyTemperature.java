// Brandon Hosley
// CSC320 - Programming 1
// 2018 01 25

import java.util.Scanner;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class DailyTemperature {
	public static void main (String args[]) {
		Scanner scnr = new Scanner(System.in);
		HashMap<String, Double> dataCollection = new LinkedHashMap<String, Double>();
		int sampleSize = 7;
		
		for(int i = 0; i < sampleSize; i++) {
			String day;
			double temp;
			
			System.out.println("Please type the day of the week:");
			day = scnr.nextLine();
			System.out.println("Please enter the temperature for " + day + ".");
			temp = scnr.nextDouble(); scnr.nextLine();
			
			dataCollection.put(day, temp);
		};	
		
		System.out.println("The data entered was:");
		
		Iterator<Entry<String, Double>> iterator = dataCollection.entrySet().iterator();
		while (iterator.hasNext()) {
			@SuppressWarnings("rawtypes")
			Map.Entry data = (Map.Entry)iterator.next();
			System.out.println("On " + data.getKey() + " the temperature was " + data.getValue() + " degrees.");
			iterator.remove();
		};
		
		double average = dataCollection.values().stream().mapToDouble(Number::intValue).sum() / sampleSize;
		System.out.println("");
		System.out.println("The average temperature over these " + sampleSize + " days was " + average + ".");
		
		scnr.close();
	}
}
