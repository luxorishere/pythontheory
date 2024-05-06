package javap;

public class javaclass {
    public static void main(String[] args) {
        LinkedList ilist = new LinkedList();
        ilist.insert(0);
        ilist.insert(0);
        ilist.insert(0);
        ilist.insert(0);
        ilist.printing();


    }
}
class Node{
    int data;
    Node next;

    Node(int data){
        this.data = data;
    }
} 
class LinkedList{
    Node head;

    LinkedList(){
        this.head = null;
    } 
    void insert(int data){
        Node nen = new Node(data);
        if (head == null){
            head.next = nen;
        }
        else{
        
            Node temp = head;
            while (temp.next != null){
                temp = temp.next;
            }
            
            temp.next = nen;
        }
    }
    
    void printing(){
        Node temp = head;
        while (temp != null){
            System.out.println(temp.data);
            temp = temp.next;
            
        }
        

    }
}
