import java.util.*;
public class Hello {
    static int count=0;
    Scanner scan;
    class Node{
        Node left,right;
        int val;
        Node(int val){
            this.val=val;
            left=null;right=null;
        }
    }
    public Node insert(Node node,int val){
        if(node==null)return new Node(val);
        if(val< node.val)node.left=insert(node.left,val);
        else node.right=insert(node.right,val);
        return node;
    }
    public static int getCountOfLeaves(Node node){
        if(node==null)return 0;
        if(node.left==null && node.right ==null){
            return 1;
        }
        return getCountOfLeaves(node.left)+getCountOfLeaves(node.right);
    }
    public static void main(String[] args) {
        Node head=new Hello().fun(null);
        int var=getCountOfLeaves(head);
        System.out.print(var);
    }
    public Node fun(Node head)
    {
        scan=new Scanner(System.in);

        while(scan.hasNext()){
            head=insert(head,scan.nextInt());
        }
        return head;
    }
}