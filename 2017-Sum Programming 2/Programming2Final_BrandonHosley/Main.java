import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.border.EmptyBorder;
import javax.swing.Box;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;

public class Main extends JFrame {
	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JPanel dataEntryPanel = new JPanel();
	private JTextField nameField = new JTextField(10);
    private JTextField gradeField = new JTextField(4);
    
	protected static HashMap<String,String> gradebook = new HashMap<String,String>() {
		private static final long serialVersionUID = 1L;
		//for Testing
		//{put("Brandon","90");put("Cara","90");put("John","80");put("Meredith","90");}
	};
	static DefaultListModel<String> roster = new DefaultListModel<String>();	
	private static JList<String> rosterView = new JList<String>(roster);
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main frame = new Main();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Main() {
		refreshRoster();
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 249, 339);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		/*
		 * Data Entry Dialogue
		 */

		dataEntryPanel.add(new JLabel("Student Name:"));
		dataEntryPanel.add(nameField);
		dataEntryPanel.add(Box.createHorizontalStrut(15)); // a spacer
		dataEntryPanel.add(new JLabel("Grade:"));
		dataEntryPanel.add(gradeField);
		
		/*
		 * Main GUI
		 */
		
		JButton btnAdd = new JButton("Add");
		btnAdd.setBounds(12, 13, 97, 25);
		contentPane.add(btnAdd);
		btnAdd.addActionListener( new addNew() );
		
		JButton btnEdit = new JButton("Edit");
		btnEdit.setBounds(12, 45, 97, 25);
		contentPane.add(btnEdit);
		btnEdit.addActionListener( new editSelected() );
		
		JButton btnDelete = new JButton("Delete");
		btnDelete.setBounds(12, 77, 97, 25);
		contentPane.add(btnDelete);
		btnDelete.addActionListener( new deleteSelected() );
		
		JButton btnPrint = new JButton("Print");
		btnPrint.setBounds(121, 77, 97, 25);
		contentPane.add(btnPrint);
		btnPrint.addActionListener( new printGrades() );
		
		JButton btnLoad = new JButton("Load");
		btnLoad.setBounds(121, 13, 97, 25);
		contentPane.add(btnLoad);
		btnLoad.addActionListener( new loadGrades() );
		
		JButton btnSave = new JButton("Save");
		btnSave.setBounds(121, 45, 97, 25);
		contentPane.add(btnSave);
		btnSave.addActionListener( new saveGrades() );
		
		rosterView.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		JScrollPane rosterScroller = new JScrollPane(rosterView);
		contentPane.add(rosterScroller);
		rosterScroller.setBounds(22, 115, 186, 151);
	}
	
	/*
	 * Action Listeners
	 */
	
	public class addNew implements ActionListener{
		public void actionPerformed(ActionEvent arg0) {
			
			nameField.setText(""); //empty the fields when the dialogue appears.
			gradeField.setText(""); //otherwise the field will hold the data from the last add action.
			
			int result = JOptionPane.showConfirmDialog(null,dataEntryPanel,"Please Enter Student Name and Grade",JOptionPane.OK_CANCEL_OPTION);
		      if (result == JOptionPane.OK_OPTION) {
		    	  String name = nameField.getText();
		    	  String grade = gradeField.getText();
		    	  gradebook.put( name , grade );
		    	  refreshRoster();
		    	  
		    	  //For Testing
		    	  System.out.println("Name: " + name);
		    	  System.out.println("Grade: " + grade); 
		      }	
		}//end action
	}//end addNew
	
	public class deleteSelected implements ActionListener{
		public void actionPerformed(ActionEvent arg0) {
			String selected = "";
			selected = rosterView.getSelectedValue();
			gradebook.remove(selected);
			refreshRoster();
			//For Testing
			System.out.println(selected + " was deleted.");
		}//end action
	}//end deleteSelected
	
	public class editSelected implements ActionListener{
		public void actionPerformed(ActionEvent arg0) {
			
			//Set the data in the data entry form to the selected person's information
			String selectedStudent = rosterView.getSelectedValue();
			String selectedGrade = gradebook.get(selectedStudent);
			nameField.setText(selectedStudent);
			gradeField.setText(selectedGrade); 
			
			int result = JOptionPane.showConfirmDialog(null,dataEntryPanel,"Please Enter Student Name and Grade",JOptionPane.OK_CANCEL_OPTION);
		      if (result == JOptionPane.OK_OPTION) {
		    	  gradebook.remove(selectedStudent); //remove the selected entry
		    	  String name = nameField.getText(); 
		    	  String grade = gradeField.getText();
		    	  gradebook.put( name , grade );	// reenter the data as though new
		    	  refreshRoster();
		    	  
		    	  //For Testing
		    	  System.out.println("Name: " + name);
		    	  System.out.println("Grade: " + grade);
		      }	
		}//end action
	}//end editSelected
	
	public class loadGrades implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			gradebook.clear();
			FileHelper.load(gradebook, "gradebook.ser");
			refreshRoster();
		}//end Action
	}//end loadGrades
	
	public class saveGrades implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			FileHelper.save(gradebook, "gradebook.ser");	
		}//end Action
	}//end saveGrades
	
	public class printGrades implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			try {
				FileHelper.printer(gradebook, "Gradebook.txt");
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}//end Action
	}//end printGrades
	
	/*
	 * Helpers
	 */
	
	public static void refreshRoster(){
		String[] studentList = new String[gradebook.size()];
		gradebook.keySet().toArray(studentList);
		Arrays.sort(studentList);
		roster.removeAllElements();
		for (String s :studentList) {
			roster.addElement(s);
		};
		//For Testing
		System.out.println( Arrays.toString(studentList) );
	}
}
