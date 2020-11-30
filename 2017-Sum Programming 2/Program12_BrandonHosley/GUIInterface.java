/*
 * Brandon Hosley
 * 
 * Project Name: CSC372-CTA01-A
 * 
 * Project Purpose: This project is intended to be a demonstration of basic proficiency in creating a simple Java GUI
 * 
 * Algorithm Used: javax.swing.* classes are used to implement GUI objects with basic event listeners, and responsiveness.
 * 
 * Inputs: User will input a date of birth into three fields corresponding to day, month, and year.
 * 
 * Outputs: The program will have a panel dedicated to returning the age value that corresponds to today's date and the DoB provided by the user.
 * 			The outputs will be formatted into age in years, months, days, hours, and seconds.
 * 
 * Limitations:	The program is simply a calculator for this very specific usage. Its functionality is limited to calculating age and nothing more.
 * 
 * Errors: Error 1: User reports error in age calculation. Error is replicated and confirmed. Problem is properly passing spinner value to actionHandler.
 * 				Solution: 	1) Make spinner component accessible to Interface class methods.
 * 							2) In calculate method pass spinner value as object to a holder variable
 * 							3) Declare a date object passing it the object in the holder variable casting the date type.
 * 							4) Using this new date as the variable passed into the Age.message() method.
 * 
 * ==================
 */

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JSpinner;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.UIManager;
import javax.swing.SpinnerDateModel;
import java.util.Date;
import java.util.Calendar;

@SuppressWarnings("serial")
public class GUIInterface extends JFrame {

	private JPanel contentPane;
	static Long defaultdate = 0000000000001L; //Default DoB, Which is 1ms after UNIX Epoch
	static JSpinner spinner = new JSpinner();
	
	/*
	 * Launch the application.
	 */
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GUIInterface frame = new GUIInterface();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			
		});
	}

	/*
	 * Create the frame.
	 */
	
	public GUIInterface() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 310, 199);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnCalculate = new JButton("CALCULATE!");
		btnCalculate.setBounds(161, 90, 119, 29);
		contentPane.add(btnCalculate);
		btnCalculate.addActionListener(new Calculate());
		
		JTextArea txtrInstructions = new JTextArea();
		txtrInstructions.setBackground(UIManager.getColor("Button.background"));
		txtrInstructions.setEditable(false);
		txtrInstructions.setWrapStyleWord(true);
		txtrInstructions.setLineWrap(true);
		txtrInstructions.setText("Please enter your date of birth so that we may calculate your exact age.");
		txtrInstructions.setBounds(12, 13, 253, 58);
		contentPane.add(txtrInstructions);
		
		spinner.setModel(new SpinnerDateModel(new Date(defaultdate), null, null, Calendar.MILLISECOND));
		spinner.setBounds(12, 84, 137, 40);
		contentPane.add(spinner);
	}
	
	/*
	 * Action Listeners
	 */
	
	static class Calculate implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			Object input = spinner.getValue();
			Date birthdate = (Date)input;
			long ageMS = System.currentTimeMillis() - birthdate.getTime();
			
			JFrame f = new JFrame();
			JOptionPane.showMessageDialog(f, Age.message(ageMS));
		}
	}
	
}
