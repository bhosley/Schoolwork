import java.awt.Color;
import java.util.Random;

public class Chromo {
	private Color currentColor = new Color(250, 250, 250);
	Random rando = new Random();
	
	public Chromo() {
		
	}
	
	public Color current() {
		return currentColor;
	}
	
	public void change() {
		int r = rando.nextInt(255);
		int g = rando.nextInt(255);
		int b = rando.nextInt(255);
		Color newColor = new Color(r,g,b);
		currentColor = newColor;
	}
}
