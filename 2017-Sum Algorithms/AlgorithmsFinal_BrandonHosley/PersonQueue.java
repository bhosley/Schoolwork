
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.Queue;

public class PersonQueue implements Queue<Person>{
	ArrayList<Person> contents = new ArrayList<Person>();
	
	/*
	 * Custom Methods
	 */
	
	//default constructor
	public PersonQueue() {}
	
	//copy constructor
	@SuppressWarnings("unchecked")
	public PersonQueue(PersonQueue original) {
	    this.contents = (ArrayList<Person>) original.contents.clone();
	}
	
	public void sortByLastName() {
		Sort.quicksort(contents, "lName");
	}
	
	public void sortByFirstName() {
		Sort.quicksort(contents, "fName");
	}
	
	public void sortByAge() {
		Sort.quicksort(contents, "age");
	}
	
	/*
	 * Standard Queue Methods
	 */

	@Override
	public boolean addAll(Collection<? extends Person> c) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public void clear() {
		contents = new ArrayList<Person>();
	}

	@Override
	public boolean contains(Object o) {
		return contents.contains(o);
	}

	@Override
	public boolean containsAll(Collection<?> c) {
		return contents.containsAll(c);
	}

	@Override
	public boolean isEmpty() {
		return contents.isEmpty();
	}

	@Override
	public Iterator<Person> iterator() {
		return contents.iterator();
	}

	@Override
	public boolean remove(Object o) {
		return contents.remove(o);
	}

	@Override
	public boolean removeAll(Collection<?> c) {
		return contents.removeAll(c);
	}

	@Override
	public boolean retainAll(Collection<?> c) {
		return contents.retainAll(c);
	}

	@Override
	public int size() {
		return contents.size();
	}

	@Override
	public Object[] toArray() {
		return contents.toArray();
	}

	@Override
	public <T> T[] toArray(T[] a) {
		return contents.toArray(a);
	}

	@Override
	public boolean add(Person e) {
		return contents.add(e);
	}

	@Override
	public Person element() {
		return null;
	}

	@Override
	public boolean offer(Person e) {
		return contents.add(e);
	}

	@Override
	public Person peek() {
			return contents.get(0);
	}

	@Override
	public Person poll() {
		Person p = contents.get(0);
		contents.remove(0);
		return p;	
	}

	@Override
	public Person remove() {
		if (contents.isEmpty()) {
			throw new IndexOutOfBoundsException("Queue is empty.");
		} else {
			Person p = contents.get(0);
			contents.remove(0);
			return p;
		}		
	}	
	
}
