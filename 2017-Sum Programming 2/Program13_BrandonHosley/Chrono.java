import java.util.Date;
import java.text.SimpleDateFormat;


public class Chrono {
	
	public String getTime() {	
		return getData("time", "HH:mm:ss");
	}
	
	public String getDate() {
		return getData("date", "dd-MM-yyyy");
	}
	
	public String getData(String name, String format) {
		String data = new SimpleDateFormat(format).format(new Date());
		String text = String.format("The current %s is:\n%s", name, data);
		return text;
	}
	
}
