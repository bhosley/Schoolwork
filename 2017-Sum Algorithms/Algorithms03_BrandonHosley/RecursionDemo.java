
public class RecursionDemo {
	
	public static int[] reverse(int[] arr) {
		return reverse(arr, 0);
	}
	
	public static int[] reverse(int[] arr, int i) {
		if (i > (arr.length - i - 1)) {
			return arr;
		} else {
			int holder = arr[i];
			arr[i] = arr[arr.length - i - 1];
			arr[arr.length - i - 1] = holder;
			return reverse(arr, i + 1);
		}
	}//end reverse
	
}//end demo
