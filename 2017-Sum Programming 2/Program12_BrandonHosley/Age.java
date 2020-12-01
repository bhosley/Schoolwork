public class Age {
	
	public static String message (long ageMS) {
		long ageS = ageMS / 1000;
		long ageMin = ageS / 60;
		long ageH = ageMin / 60;
		long ageD = ageH / 24;
		long ageY = ageD / 365;
		long ageMon = ageY * 12;
		
		String text = "A person with that date of birth is:\n" +
				ageMS + " Milliseconds,\n" +
				ageS + " Seconds,\n" +
				ageMin + " Minutes,\n" +
				ageH + " Hours,\n" +
				ageD + " Days,\n" +
				ageMon + " Months, or\n" +
				ageY + " Years old.\n" +
				"Wow! ";
		return text;
	}
	
}
