/*
 * Brandon Hosley
 * 
 * Project Name: CSC372-CTA01-A
 * 
 * Project Purpose: This project is intended to be a demonstration of basic proficiency in creating a simple Java GUI
 * 
 * Algorithm Used: javax.swing.* classes are used to implement GUI objects with basic event listeners, and responsiveness.
 * 
 * Inputs: User will not be required to input any data, but will be able to interact with a point and click device.
 * 
 * Outputs: The program will have a panel dedicated to displaying the current date or time depending on which button the user clicks.
 * 			Additionally, the background will change color each time the user clicks on either button.
 * 
 * Limitations:	The program is an interactive display device that will show the date or time as the user wills. It will also feature fun background color changes.
 * 
 * Errors:
 * 
 * ==================
 */

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;
import javax.swing.JButton;
import javax.swing.JTextPane;

public class GUI extends JFrame {
	private static final long serialVersionUID = 1L;
	private static JPanel contentPane;
	protected static Chromo background = new Chromo();
	protected static JTextPane display = new JTextPane();
	protected static Chrono displayData = new Chrono();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GUI frame = new GUI();
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
	public GUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 252, 206);
		contentPane = new JPanel();
		contentPane.setBackground(background.current());
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnShowDate = new JButton("Show Date");
		btnShowDate.setBounds(12, 13, 97, 25);
		contentPane.add(btnShowDate);
		btnShowDate.addActionListener(new displayDate());
		
		JButton btnShowTime = new JButton("Show Time");
		btnShowTime.setBounds(125, 13, 97, 25);
		contentPane.add(btnShowTime);
		btnShowTime.addActionListener(new displayTime());
		
		//JTextArea txtrT = new JTextArea();
		display.setBounds(22, 51, 183, 63);
		contentPane.add(display);
		
		JButton btnExit = new JButton("Exit");
		btnExit.setBounds(68, 127, 97, 25);
		btnExit.addActionListener(new exitButton());
		contentPane.add(btnExit);
		StyledDocument style = display.getStyledDocument();
		//center the display text
		SimpleAttributeSet center = new SimpleAttributeSet();
		StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER);
		style.setParagraphAttributes(0, style.getLength(), center, false);
	}
	
	/*
	 * Action Listeners
	 */
	
	static class displayDate implements ActionListener{
		public void actionPerformed(ActionEvent Arg0) {
			String text = displayData.getDate();
			changeText(text);
			
			background.change();
			contentPane.setBackground(background.current());
		}
	}
	
	static class displayTime implements ActionListener{
		public void actionPerformed(ActionEvent Arg0) {
			String text = displayData.getTime();
			changeText(text);
			
			background.change();
			contentPane.setBackground(background.current());
		}
	}
	
	static void changeText(String content) {
		display.setText(content);
	}
	
	private class exitButton implements ActionListener{
	    @Override
	    public void actionPerformed(ActionEvent e) {
	        System.exit(0);
	    }
	}
}
