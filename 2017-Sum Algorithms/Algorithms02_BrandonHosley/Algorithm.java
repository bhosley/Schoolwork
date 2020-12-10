import java.util.Stack;

public class Algorithm {

	public static int evaluatePostFix(String postFix) {
		/*
		 * Order of operations is ignored as order is implicit in arithmetic that has been converted to postfix format
		 * Currently this method only supports integer evaluation
		 */

		Stack<Integer> stack = new Stack<Integer>();
	    int val1 = 0;
	    int val2 = 0;
	    String[] str = postFix.split(" ");


	    for(int i =0; i<str.length; i++){
	        if(Character.isDigit(str[i].charAt(0))){
	            stack.push(Integer.parseInt(str[i]));
	        }
	        else
	        {
	            val2 = stack.pop();
	            val1 = stack.pop();

	            switch(str[i].charAt(0))
	            {
	            	case '+': stack.push(val1 + val2);
	                break;

	            	case '-': stack.push(val1 - val2);
	            	break;

	            	case '/': stack.push(val1 / val2);
	            	break;
	            	
	            	case '*': stack.push(val1 * val2) ;
	                break;
	            }
	        }
	    }//end for
	    
	    return stack.pop();
	    
	}//end evaluatePostFix
	
}// Class Algorithm
