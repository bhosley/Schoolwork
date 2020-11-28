import java.math.BigDecimal;

public class RecursionDemo {
	
	
	public static Number calculateSum(Number[] array) {
		return calculateSum(array, array.length-1);
	}

	public static Number calculateSum(Number[] array, int i) {
		if (i == 0)
			//recursion base case: first item in the array.
			return array[i];
		else
			//return array[i] + calculateSum(array, i-1);
			return new BigDecimal( array[i].floatValue() ).add( new BigDecimal( calculateSum(array, i-1).floatValue() ) );
	}//end Sum
	
	
	public static Number calculateProduct(Number[] array) {
		return calculateProduct(array, array.length-1);
	}
	
	public static Number calculateProduct(Number[] array, int i) {
		if (i == 0)
			//recursion base case: first item in the array.
			return array[i];
		else
			return new BigDecimal( array[i].floatValue() ).multiply( new BigDecimal( calculateProduct(array, i-1).floatValue() ) );
	}//end Product
}
