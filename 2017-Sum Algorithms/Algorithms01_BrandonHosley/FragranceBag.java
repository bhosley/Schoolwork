
public class FragranceBag<T> implements BagInterface<T> {
	
	private final T[] bag;
	private static final int DEFAULT_CAPACITY = 20;
	private int numberOfEntries;
	
	/*
	 * Constructors
	 */
	
	public FragranceBag() {
		this(DEFAULT_CAPACITY);
	}

	public FragranceBag(int capacity) {
		numberOfEntries = 0;
		@SuppressWarnings("unchecked")
		T[] tempBag = (T[])new Object[capacity];
		bag = tempBag;
	}
	
	public boolean add(T newEntry) {
		boolean result = true;
		if (isFull()) 
		{
			result = false;
		} else {
			bag[numberOfEntries] = newEntry;
			numberOfEntries++;
		}
		return result;
	}
	
	public T[] toArray() {
		@SuppressWarnings("unchecked")
		T[] result = (T[])new Object[numberOfEntries];
		for (int index = 0; index < numberOfEntries; index++) {
			result[index] = bag[index];
		}
		return result;
	}
	
	public boolean isFull() {
		return numberOfEntries == bag.length;
	}
	
	public T remove(int index) {
		T trash = bag[index];
		bag[index] = null;
		return trash;
	}
	
	public boolean remove(T item) {
		if (this.contains(item)) {
			int i = this.getIndexOf(item);
			this.remove(i);
			return true;
		} else {
			return false;
		}
	}
	
	public int getIndexOf(T item) {
			int i = 0;
			for(int j=0; j<bag.length; j++) {
				if (bag[j] == item) {
					i = j;
				}
			}
			return i;
	}
	
	public void clear(){
		for(int i=0;i<bag.length;i++) {
			bag[i] = null;
		}
	}

	public int getCurrentSize() {
		int size = 0;
		for(int i=0; i<bag.length; i++) {
			if (bag[i] != null){
				size++;
			}
		}
		return size;
	}

	public boolean isEmpty() {
		return !(numberOfEntries == bag.length);
	}

	public int getFrequencyOf(T item) {
		int freq = 0;
		for(int i=0; i<bag.length; i++) {
			if (bag[i] != item){
				freq++;
			}
		}
		return freq;
	}

	public boolean contains(T item) {
		boolean result = false;
		for (int i=0; i<bag.length; i++) {
			if(bag[i] == item) {
				result = true;
			}
		}
		return result;
	}

}
