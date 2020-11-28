import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import javax.swing.JOptionPane;

public class FileHelper {
	
	public static void save(HashMap<String,String> hm, String filename) {
		try{
			FileOutputStream fos = new FileOutputStream(filename);
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			oos.writeObject(hm);
			oos.close();
			fos.close();
			System.out.printf("Serialized HashMap data is saved in hashmap.ser");
		} catch(IOException ioe) {
			ioe.printStackTrace();
		}
	}//end save
	
	@SuppressWarnings("unchecked")
	public static void load(HashMap<String, String> hm, String filename) {
		HashMap<String, String> tempMap = null;
		try{
			FileInputStream fis = new FileInputStream(filename);
	         ObjectInputStream ois = new ObjectInputStream(fis);
	         tempMap = (HashMap<String, String>) ois.readObject();
	         ois.close();
	         fis.close();
	      } catch(IOException ioe) {
	    	  ioe.printStackTrace();
	    	  return;
	      }catch(ClassNotFoundException c) {
	    	  System.out.println("Class not found");
	    	  c.printStackTrace();
	    	  return;
	      }
		System.out.println("Deserialized HashMap..");
		// Display content using Iterator
		Set<?> set = tempMap.entrySet();
		Iterator<?> iterator = set.iterator();
	      while(iterator.hasNext()) {
	         @SuppressWarnings("rawtypes")
			Map.Entry mentry = (Map.Entry)iterator.next();
	         String key = (String) mentry.getKey();
	         String value = (String) mentry.getValue();
	         hm.put( key , value );
	         System.out.print("key: "+ key + " & Value: ");
	         System.out.println(value);
	      }
	}//end load
	
	public static void printer(HashMap<String, String> hm, String filename) throws IOException {
		//Build a printer and place to print to
		File gradeFile = new File(filename);
		if( !gradeFile.exists() ){ gradeFile.createNewFile(); }
		PrintWriter printer = new PrintWriter(gradeFile);
		
		//Array the entries
		String[] gradeArray = new String[hm.size()];
		int i = 0;
		for(Map.Entry<String, String> student : hm.entrySet()) {
			String output = String.format( "%-25s%-15s\n", student.getKey(), student.getValue() );
			gradeArray[i] = output;
			i++;
		}
		
		//Sort the array and convert to a single string
		StringBuilder runningText = new StringBuilder("The students and grades for this course:\n");
		Arrays.sort(gradeArray);
		for(String g : gradeArray ) {
			runningText.append(g);
		}
		
		//Output text to appropriate places
		printer.print(runningText);
		System.out.print(runningText);
		printer.close();
		System.out.println("Export was successful.");
		JOptionPane.showMessageDialog(null,"The following was saved to " + filename + "\n\n" + runningText);
	}//end printer
	
}
