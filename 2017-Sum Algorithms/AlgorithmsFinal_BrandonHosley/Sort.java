import java.util.ArrayList;

public class Sort {
	
	public static void quicksort(ArrayList<Person> list, String sortType) {
		quickSort(list, 0, list.size() - 1, sortType);
	}
	
	private static void quickSort(ArrayList<Person> list, int left, int right, String sortType)
	{
	    if (left >= right)
	    {
	        return;
	    }
	    int pivot = choosePivot(list, left, right, sortType);
	    pivot = partition(list, pivot, left, right, sortType);
	    quickSort(list, left, pivot - 1, sortType);
	    quickSort(list, pivot + 1, right, sortType);
	}
	
	private static int partition(ArrayList<Person> list, int pivot, int left, int right, String sortType)
	{
	    swap(list, pivot, left);
	    pivot = left;
	    int i = left + 1;
	    for (int j = left + 1; j <= right; j++)
	    {
	        if (comparator(list, j, pivot, sortType) )
	        {
	            swap(list, j, i);
	            i++;
	        }
	    }
	    swap(list, pivot, i - 1);
	    return i - 1;
	}
	
	private static void swap(ArrayList<Person> list, int j, int i)
	{
	    Person temp = list.get(j);
	    list.set(j, list.get(i));
	    list.set(i, temp);
	}
	
	private static boolean comparator(ArrayList<Person> list, int a, int b, String sortType) {
		switch (sortType) {
		case "fName": return list.get(a).getFirstName().compareTo(list.get(b).getFirstName())<0;
		case "lName": return list.get(a).getLastName().compareTo(list.get(b).getLastName())<0;
		case "age": return list.get(a).getAge() < list.get(b).getAge();
		default: return list.get(a).getLastName().compareTo(list.get(b).getLastName())<0; //should never return this one.
		} 
	}
	
	private static int choosePivot(ArrayList<Person> list, int left, int right, String sortType)
	{
	    return medianOfThree(list, left, (left + right) / 2, right, sortType);
	    // return right;
	}
	
	private static int medianOfThree(ArrayList<Person> list, int aIndex, int bIndex, int cIndex, String sortType)
	{
	    int largeIndex, smallIndex;
	    //if (a>b)
	    if( comparator(list, bIndex, aIndex, sortType) )
	    {
	        largeIndex = aIndex;
	        smallIndex = bIndex;
	    }
	    else
	    {
	        largeIndex = bIndex;
	        smallIndex = aIndex;
	    }
	    //if (c > array[largeIndex])
	    if( comparator(list, largeIndex, cIndex, sortType) )
	    {
	        return largeIndex;
	    }
	    else
	    {
	        //if (c < array[smallIndex])
	    	if( comparator(list, cIndex, smallIndex, sortType) )
	        {
	            return smallIndex;
	        }
	        else
	        {
	            return cIndex;
	        }
	    }
	}
	
}
