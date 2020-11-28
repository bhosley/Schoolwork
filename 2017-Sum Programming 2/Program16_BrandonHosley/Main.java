/*
 * Brandon Hosley
 * 
 * Project Name: CSC372-CTA01-A
 * 
 * Project Purpose: Demonstrate knowledge of basic sorting algorithms by writing a program that will sort a 
 * list of names in alphabetical and reverse orders.
 * 
 * Algorithm Used: Selection sort, Merge Sort 
 * 
 * Inputs: 10 names in the form of <Strings>.
 * 
 * Outputs: Will output the list of names in alphabetical or reverse-alpha order.
 * 
 * Limitations:
 * 
 * Errors: 
 * 
 * ==================
 */

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.awt.event.ActionEvent;

public class Main extends JFrame {
	private static final long serialVersionUID = 1L;
	
	private JPanel contentPane;
	private JTextField textField0;
	private JTextField textField2;
	private JTextField textField1;
	private JTextField textField3;
	private JTextField textField4;
	private JTextField textField5;
	private JTextField textField6;
	private JTextField textField7;
	private JTextField textField8;
	private JTextField textField9;

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
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 285, 343);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField0 = new JTextField();
		textField0.setBounds(12, 47, 116, 22);
		contentPane.add(textField0);
		textField0.setColumns(10);
		
		textField2 = new JTextField();
		textField2.setBounds(12, 82, 116, 22);
		contentPane.add(textField2);
		textField2.setColumns(10);
		
		textField1 = new JTextField();
		textField1.setBounds(140, 47, 116, 22);
		contentPane.add(textField1);
		textField1.setColumns(10);
		
		textField3 = new JTextField();
		textField3.setBounds(140, 82, 116, 22);
		contentPane.add(textField3);
		textField3.setColumns(10);
		
		textField4 = new JTextField();
		textField4.setBounds(12, 117, 116, 22);
		contentPane.add(textField4);
		textField4.setColumns(10);
		
		textField5 = new JTextField();
		textField5.setBounds(140, 117, 116, 22);
		contentPane.add(textField5);
		textField5.setColumns(10);
		
		textField6 = new JTextField();
		textField6.setBounds(12, 152, 116, 22);
		contentPane.add(textField6);
		textField6.setColumns(10);
		
		textField7 = new JTextField();
		textField7.setBounds(140, 152, 116, 22);
		contentPane.add(textField7);
		textField7.setColumns(10);
		
		textField8 = new JTextField();
		textField8.setBounds(12, 187, 116, 22);
		contentPane.add(textField8);
		textField8.setColumns(10);
		
		textField9 = new JTextField();
		textField9.setBounds(140, 187, 116, 22);
		contentPane.add(textField9);
		textField9.setColumns(10);
		
		JLabel instructionBox = new JLabel("Please enter the names to be sorted.");
		instructionBox.setBounds(12, 13, 243, 21);
		contentPane.add(instructionBox);
		
		JButton btnSortAlpha = new JButton("Sort Alphabetically");
		btnSortAlpha.setBounds(55, 219, 148, 29);
		contentPane.add(btnSortAlpha);
		btnSortAlpha.addActionListener(new sortAlpha());
		
		JButton btnSortRev = new JButton("Sort Reversed");
		btnSortRev.setBounds(55, 259, 148, 27);
		contentPane.add(btnSortRev);
		btnSortRev.addActionListener(new sortRev());
	}
	
	/*
	 * Action Listeners
	 */
	
	public class sortAlpha implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			displayResult(Sort.alphabetical(loadData()));
		}//end Action	
	}//end sortAlpha
	
	public class sortRev implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			displayResult(Sort.reverse(loadData()));
		}//end Action
	}//end sortRev
	
	/*
	 * Action Helpers
	 */
	
	public void displayResult(ArrayList<String> list) {
		String text = "";
		for(String name : list) text += name + "\n";
		JOptionPane.showMessageDialog(null, text);
	}//end displayResult
	
	public ArrayList<String> loadData(){
		ArrayList<String> temp = new ArrayList<String>();

		if(!textField0.getText().trim().equals("")) { temp.add(textField0.getText()); };
		if(!textField1.getText().trim().equals("")) { temp.add(textField1.getText()); };
		if(!textField2.getText().trim().equals("")) { temp.add(textField2.getText()); };
		if(!textField3.getText().trim().equals("")) { temp.add(textField3.getText()); };
		if(!textField4.getText().trim().equals("")) { temp.add(textField4.getText()); };
		if(!textField5.getText().trim().equals("")) { temp.add(textField5.getText()); };
		if(!textField6.getText().trim().equals("")) { temp.add(textField6.getText()); };
		if(!textField7.getText().trim().equals("")) { temp.add(textField7.getText()); };
		if(!textField8.getText().trim().equals("")) { temp.add(textField8.getText()); };
		if(!textField9.getText().trim().equals("")) { temp.add(textField9.getText()); };
		
		
		return temp;
	}
	/* 
	 * Text Field Getters
	 * 
	protected JTextField getTextField0() {
		return textField0;
	}
	protected JTextField getTextField1() {
		return textField1;
	}
	protected JTextField getTextField9() {
		return textField9;
	}
	protected JTextField getTextField3() {
		return textField3;
	}
	protected JTextField getTextField6() {
		return textField6;
	}
	protected JTextField getTextField7() {
		return textField7;
	}
	protected JTextField getTextField8() {
		return textField8;
	}
	protected JTextField getTextField2() {
		return textField2;
	}
	protected JTextField getTextField4() {
		return textField4;
	}
	protected JTextField getTextField5() {
		return textField5;
	}
	*/
	
}


