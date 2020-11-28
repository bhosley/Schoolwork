/*
 * Brandon Hosley
 * 
 * Project Name: CSC372-CTA01-A
 * 
 * Project Purpose: This project is intended to be a demonstration of using recursive methods to solve basic a basic repetitive problem.
 * 
 * Algorithm Used: A recursive method is used to find the sum or product of five integers in an array. 
 * 
 * Inputs: Five <Number>-only fields that accept numeral characters. Non-numeric cells are treated as zero.
 * 
 * Outputs: Will output the product or the sum of the five fields depending on which button the user clicks on.
 * 		As blank cells are treated as zero, any blanks will yield a product of 0.
 * 
 * Limitations:	Users must enter in valid numbers. The program will ignore letter characters and will not alert the user.
 * 
 * Errors: IntFormat changed to allow negative and floating point numbers to be used as input.
 * 
 * ==================
 */

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.NumberFormat;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.text.NumberFormatter;
import javax.swing.JButton;
import javax.swing.JFormattedTextField;

public class Main extends JFrame {
	
	private static final long serialVersionUID = 1L;	
	private JPanel contentPane;
	private JFormattedTextField numField0;
	private JFormattedTextField numField1;
	private JFormattedTextField numField2;
	private JFormattedTextField numField3;
	private JFormattedTextField numField4;

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
		
		//frame
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 311, 122);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		//action buttons
		
		JButton sumButton = new JButton("Get Sum!");
		sumButton.setBounds(12, 45, 123, 25);
		contentPane.add(sumButton);
		sumButton.addActionListener(new showSum());
		
		JButton productButton = new JButton("Get Product!");
		productButton.setBounds(156, 45, 123, 25);
		contentPane.add(productButton);
		productButton.addActionListener(new showProduct());
		
		//int field formatter/protection
		
		NumberFormat format = NumberFormat.getInstance();
	    NumberFormatter intFormat = new NumberFormatter(format);
	    intFormat.setValueClass(Integer.class);
	    intFormat.setMinimum(0);
	    intFormat.setMaximum(Integer.MAX_VALUE);
	    intFormat.setAllowsInvalid(false);
	    intFormat.setCommitsOnValidEdit(true); 
	    
	    NumberFormatter numFormat = new NumberFormatter(format);
	    numFormat.setValueClass(Number.class);
	    
	    //int fields
		
		numField0 = new JFormattedTextField(numFormat);
		numField0.setBounds(12, 13, 48, 22);
		contentPane.add(numField0);
		
		numField1 = new JFormattedTextField(numFormat);
		numField1.setBounds(67, 13, 48, 22);
		contentPane.add(numField1);
		
		numField2 = new JFormattedTextField(numFormat);
		numField2.setBounds(123, 13, 48, 22);
		contentPane.add(numField2);
		
		numField3 = new JFormattedTextField(numFormat);
		numField3.setBounds(177, 13, 48, 22);
		contentPane.add(numField3);
		
		numField4 = new JFormattedTextField(numFormat);
		numField4.setBounds(231, 13, 48, 22);
		contentPane.add(numField4);
	}//end MainFrame
	
	/*
	 * Action Listeners
	 */
	
	public class showSum implements ActionListener {
		public void actionPerformed(ActionEvent Arg0) {
			
			Number data[] = loadData();
			String result = "The sum of those numbers is:\n" + RecursionDemo.calculateSum(data) ;
			displayResult(result);
			
		}//end action
	}//end showSum
	
	public class showProduct implements ActionListener {
		public void actionPerformed(ActionEvent Arg0) {
			
			Number data[] = loadData();
			String result = "The product of those numbers is:\n" + RecursionDemo.calculateProduct(data) ;
			displayResult(result);
			
		}//end action
	}//end showProduct
	
	/*
	 * ActionListener Support Functions
	 */
	
	public void displayResult(String text) {
		JOptionPane.showMessageDialog(null, text);
	}//end displayResult
	
	public Number[] loadData() {
		Number array[] = new Number[5];
		//array[0] = Integer.parseInt(numField0.getText());
		array[0] = numField0.getText().trim().equals("") ? 0 : tryParse(numField0.getText());
		array[1] = numField1.getText().trim().equals("") ? 0 : tryParse(numField1.getText());
		array[2] = numField2.getText().trim().equals("") ? 0 : tryParse(numField2.getText());
		array[3] = numField3.getText().trim().equals("") ? 0 : tryParse(numField3.getText());
		array[4] = numField4.getText().trim().equals("") ? 0 : tryParse(numField4.getText());
		return array;
	}
	
	private static Number tryParse(String str) {
	    Number number = null;
	    try {
	        number = Float.parseFloat(str);
	    } catch(NumberFormatException e) {
	        try {
	            number = Double.parseDouble(str);
	        } catch(NumberFormatException e1) {
	            try {
	                number = Integer.parseInt(str);
	            } catch(NumberFormatException e2) {
	                try {
	                    number = Long.parseLong(str);
	                } catch(NumberFormatException e3) {
	                    throw e3;
	                }       
	            }       
	        }       
	    }
	    return number;
	}
	
	/*
	 * NumField Getters
	 */
	
	/*
	protected JFormattedTextField getNumField0() {
		return numField0;
	}
	protected JFormattedTextField getNumField1() {
		return numField1;
	}
	protected JFormattedTextField getNumField2() {
		return numField2;
	}
	protected JFormattedTextField getNumField3() {
		return numField3;
	}
	protected JFormattedTextField getNumField4() {
		return numField4;
	}
	*/

}
