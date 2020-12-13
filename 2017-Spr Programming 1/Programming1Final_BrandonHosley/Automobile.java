public class Automobile {
	//attributes
	private String make;
	private String model;
	private String color;
	private int year;
	private int mileage;
	
	//constructor
	public Automobile (String newMake, String newModel, String newColor, int newYear, int newMileage) {
		make = newMake;
		model = newModel;
		color = newColor;
		year = newYear;
		mileage = newMileage;
	}
	
	//attr accessors
	public String getMake(){
		return this.make;
	};
	public String getModel(){
		return model;
	};
	public String getColor(){
		return color;
	};
	public int getYear(){
		return year;
	};
	public int getMileage(){
		return mileage;
	};

	//attr updaters
	public void updateMake(String newMake){
		make = newMake;
	};
	public void updateModel(String newModel){
		model = newModel;
	};
	public void updateColor(String newColor){
		color = newColor;
	};
	public void updateYear(int newYear){
		year = newYear;
	};
	public void updateMileage(int newMileage){
		mileage = newMileage;
	};
}
