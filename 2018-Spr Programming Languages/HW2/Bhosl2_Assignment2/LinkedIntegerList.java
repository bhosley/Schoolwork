public class LinkedIntegerList {
	private Node header;
	private Node tail;
	private int memberCount;
	
	public LinkedIntegerList() {
		header = null;
		tail = null;
		memberCount = 0;
	}
	
	public LinkedIntegerList(LinkedIntegerList lil) {
		super();
		for(int i = 0; i < lil.size(); i++) {
			this.add(lil.get(i));
		}
	}
	
	public int size() {
		return memberCount;
	}
	
	public int get(int index) {
		Node n = header;
		for(int i = index; i > 0; i--) {
			n = n.getNext();
		}
		return n.getValue();
	}
	
	public void add(int val) {
		Node newMember = new Node(val,null);    
        memberCount++ ;    
        if(header == null) {
            header = newMember;
            tail = header;
        } else {
            tail.setNext(newMember);
            tail = newMember;
        }
	}
	
	public void remove(int index) {
		if (index == 0) {
            header = header.getNext();
            memberCount--; 
            return ;
        }
        if (index == memberCount) {
            Node h = header;
            Node t = header;
            while (h != tail){
                t = h;
                h = h.getNext();
            }
            tail = t;
            tail.setNext(null);
            memberCount--;
            return;
        }
        Node ptr = header;
        index = index - 1 ;
        for (int i = 1; i < memberCount - 1; i++){
            if (i == index) {
                Node tmp = ptr.getNext();
                tmp = tmp.getNext();
                ptr.setNext(tmp);
                break;
            }
            ptr = ptr.getNext();
        }
        memberCount--;
	}
	
	public boolean contains(int val) {
		boolean result = false;
		for(int i = 0; i < memberCount; i++) {
			if (this.get(i) == val) {
				result = true;
				break;
			}
		}
		return result;
	}
	
	
}

class Node {
    private int value;
    private Node next;
 
    public Node(){
        next = null;
        value = 0;
    }    
    
    public Node(int d,Node n){
        value = d;
        next = n;
    }    

    public void setNext(Node n){
        next = n;
    }    

    public void setValue(int d){
        value = d;
    }    

    public Node getNext(){
        return next;
    }  
    
    public int getValue(){
        return value;
    }
}
