import java.util.*;
class node{
    String s;
    node pre=null,next=null;
    public node(String S){
        this.s=S;
    }
}
class Strings{
    int n,m=100;
    node head=null,p=null,nx=null,temp=head;
    public Strings(){
        Scanner q=new Scanner(System.in);
        this.n=q.nextInt();
        q.nextLine();
        for(int i=0;i<n;i++){
            node temp_node=new node(q.nextLine());
            m=Math.min(m,temp_node.s.length());
            if(head==null)
            head=temp_node;
            else{
                while(temp.next!=null){
                    temp=temp.next;
                }
                temp_node.pre=temp;
                temp.next=temp_node;
            }
            temp=head;
        }
    }
    public int Length(){
        temp=head;
        int y=0;
        while(temp!=null){
            if(temp.s.length()>0)
            y++;
            temp=temp.next;
        }
        return y;
    }
    public void print(){
        int pl=Length();
        while(pl>0 ){
            temp=head;
            int tp=100;
            while(temp!=null){
                if(temp.s.length()>0){
                    System.out.println(temp.s.substring(0,Math.min(temp.s.length(),m)));
                    temp.s=temp.s.substring(Math.min(temp.s.length(),m));
                    if(temp.s.length()>0){
                        tp=Math.min(tp,temp.s.length());
                    }
                }
                temp=temp.next;
            }
            m=tp;
            pl=Length();
        }
    }
}
public class Hello {

    public static void main(String[] args) {
        Strings s=new Strings();
        s.print();
	}
}